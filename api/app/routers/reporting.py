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

    """This get request computes weekly average trips per region
    Args:
        current_user: parameter to ensure user is correctly authenticated
    Returns:
        message: json format report with computed data
    """

    print(current_user)

    # querying mysql tables to get neccesary data

    query = '''
        SELECT
            a.id,
            b.name_desc AS region,
            a.trip_datetime
        FROM trips a
        LEFT JOIN regions b
        ON a.region_id = b.id
    '''

    # reading query into a dataframe

    df = pd.read_sql(
        query,
        con = engine
    )

    # grouping by year / week to compute the weekly average trips per region

    df['year_week'] = df['trip_datetime'].dt.strftime('%Y%W')

    reporting_dict = df.groupby(['year_week', 'region']).size().groupby('region').mean().to_dict()

    return reporting_dict