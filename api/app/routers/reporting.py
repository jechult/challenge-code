from fastapi import APIRouter, Depends
from database import engine
import pandas as pd
from oatuh2 import get_current_user

router = APIRouter(
    prefix = "/reporting",
    tags = ["reporting"]
)

@router.get('/weekly')
def create_weekly_reporting(
    current_user: int = Depends(get_current_user)
):

    print(current_user)

    query = '''
        SELECT
            a.id,
            b.name_desc AS region,
            a.trip_datetime
        FROM trips a
        LEFT JOIN regions b
        ON a.region_id = b.id
    '''

    df = pd.read_sql(
        query,
        con = engine
    )

    print(df.head())

    df['year_week'] = df['trip_datetime'].dt.strftime('%Y%W')

    reporting_dict = df.groupby(['year_week', 'region']).size().groupby('region').mean().to_dict()

    return reporting_dict