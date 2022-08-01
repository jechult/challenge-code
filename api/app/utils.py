from io import BytesIO
from fastapi import UploadFile
import pandas as pd
from database import engine
from datetime import datetime
import time

CHUNKSIZE = 100000
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def process_trips_data(df: pd.DataFrame):

    """This function processes trips dataframe before inserting it into mysql trips table
    Args:
        df: Dataframe with trips data
    Returns:
        df: Processed dataframe with trips data
    """

    pattern = '[0-9]+\.[0-9]+'

    df_copy = df.copy()

    # Adding new columns about origin and destination coordinates

    df_copy['origin_coord_new'] = df_copy['origin_coord'].str.findall(pattern)
    df_copy['destination_coord_new'] = df_copy['destination_coord'].str.findall(pattern)

    df_copy['origin_x'] = df_copy['origin_coord_new'].str.get(0)
    df_copy['origin_y'] = df_copy['origin_coord_new'].str.get(1)
    df_copy['destination_x'] = df_copy['destination_coord_new'].str.get(0)
    df_copy['destination_y'] = df_copy['destination_coord_new'].str.get(1)

    df_copy['trip_datetime'] = pd.to_datetime(df_copy['datetime'])

    # dropping unused columns

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

    # changing columns type

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

    """This function reads sent file and insert into mysql table
    Args:
        table_content: sent file in upload post request
    Returns:
        message: informaton about data ingestion process
    """

    # itering content using a DataFrame list

    start_datetime = datetime.now()

    dfIter = pd.read_csv(BytesIO(table_content.file.read()), chunksize = CHUNKSIZE)

    row_count = 0

    if table_name in ('sources', 'regions'):

        for df in dfIter:

            df['name_desc'] = df['name_desc'].astype(str)

            df.to_sql(table_name, engine, index = False, if_exists = 'append')

            row_count+=df.shape[0]

            end_datetime = datetime.now()

            print(f'{datetime.strftime(end_datetime, DATE_FORMAT)}: Commited row {row_count}', flush=True)

        elapsed_time = (end_datetime - start_datetime).total_seconds()

        print(f'''{datetime.strftime(end_datetime, DATE_FORMAT)}: \
{row_count} rows were inserted in table {table_name} in {elapsed_time} seconds.''',
            flush=True)

        return {'message': f'table {table_name} updated'}
    
    elif table_name == 'trips':

        for df in dfIter:

            df_aux = process_trips_data(df)

            df_aux.to_sql(table_name, engine, index = False, if_exists = 'append')

            row_count+=df_aux.shape[0]

            end_datetime = datetime.now()

            print(f'{datetime.strftime(end_datetime, DATE_FORMAT)}: Commited row {row_count}', flush=True)
        
        elapsed_time = (end_datetime - start_datetime).total_seconds()

        print(f'''{datetime.strftime(end_datetime, DATE_FORMAT)}: \
{row_count} rows were inserted in table {table_name} in {elapsed_time} seconds.''',
            flush=True)

        return {'message': f'table {table_name} updated'}
    
    else:

        return {'message': f'table {table_name} does not exist'}
