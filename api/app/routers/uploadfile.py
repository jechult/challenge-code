from fastapi import APIRouter, File, Form, UploadFile
from utils import process_data

router = APIRouter(
    prefix = "/uploadfile",
    tags = ["uploadfile"]
)

@router.post('/')
def created_upload_file(table_name: str = Form(...), table_content: UploadFile = File(...)):

    print(table_name)

    # content = table_content.file.read()

    message = process_data(table_content, table_name)

    return {'message': message}