from fastapi import APIRouter, Depends, File, Form, UploadFile
from utils import process_data
from oatuh2 import get_current_user
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

router = APIRouter(
    prefix = "/uploadfile",
    tags = ["uploadfile"]
)

@router.post('/')
def created_upload_file(
    table_name: str = Form(...),
    table_content: UploadFile = File(...),
    current_user: int = Depends(get_current_user),
):

    """This post request receives a csv file to be processed and insert into a mysql table
    Args:
        table_name: table name where file data will be inserted
        table_content: file data to be processed before inserting into a table
        current_user: parameter to ensure user is correctly authenticated
    Returns:
        message: informaton about data ingestion process
    """

    current_dt = datetime.strftime(datetime.now(), DATE_FORMAT)

    print(f'{current_dt}: Inserting rows in table {table_name}', flush=True)

    try:

        message = process_data(table_content, table_name)
    
    except:

        return {'message': 'Sent file does not fit structure requirements'}

    return message