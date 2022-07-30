from io import BytesIO
from fastapi import UploadFile
import pandas as pd
from database import engine

CHUNKSIZE = 100000

def process_trips_data(df: pd.DataFrame):

    pattern = '[0-9]+\.[0-9]+'

    df_copy = df.copy()

    df_copy['origin_coord_new'] = df_copy['origin_coord'].str.findall(pattern)
    df_copy['destination_coord_new'] = df_copy['destination_coord'].str.findall(pattern)

    df_copy['origin_x'] = df_copy['origin_coord_new'].str.get(0)
    df_copy['origin_y'] = df_copy['origin_coord_new'].str.get(1)
    df_copy['destination_x'] = df_copy['destination_coord_new'].str.get(0)
    df_copy['destination_y'] = df_copy['destination_coord_new'].str.get(1)

    df_copy['trip_datetime'] = pd.to_datetime(df_copy['datetime'])

    df_copy.drop(
        [
        'origin_coord',
        'origin_coord_new',
        'destination_coord',
        'destination_coord_new',
        'datetime'
        ],
        axis = 1,
        inplace = True
    )

    df_copy = df_copy.astype(
        {
           'origin_x': 'float64',
           'origin_y': 'float64',
           'destination_x': 'float64',
           'destination_y': 'float64',
           'region_id': 'int64',
           'datasource_id': 'int64',
           'trip_datetime': object
        }
    )

    columns = [
        'origin_x',
        'origin_y',
        'destination_x',
        'destination_y',
        'region_id',
        'datasource_id',
        'trip_datetime'
    ]

    return df_copy[columns]

def process_data(table_content: UploadFile, table_name: str):

    # itering content using a DataFrame list

    dfIter = pd.read_csv(BytesIO(table_content.file.read()), chunksize = CHUNKSIZE)

    if table_name in ('sources', 'regions'):

        for df in dfIter:

            df['name_desc'] = df['name_desc'].astype(str)

            df.to_sql(table_name, engine, index = False, if_exists = 'append')

            return {'message': f'table {table_name} updated'}
    
    elif table_name == 'trips':

        for df in dfIter:

            df_aux = process_trips_data(df)

            df_aux.to_sql(table_name, engine, index = False, if_exists = 'append')

            return {'message': f'table {table_name} updated'}
    
    else:

        return {'message': f'table {table_name} does not exist'}
