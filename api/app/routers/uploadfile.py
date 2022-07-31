from fastapi import APIRouter, Depends, File, Form, UploadFile
from utils import process_data
from oatuh2 import get_current_user

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
    print(current_user)
    print(table_name)

    try:

        message = process_data(table_content, table_name)
    
    except:

        return {'message': 'Sent file does not fit structure requirements'}

    return {'message': message}