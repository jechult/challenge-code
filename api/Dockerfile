FROM python:3.9

LABEL maintainer="Jesus Levano <jlevanotasayco@gmail.com>"

COPY ./app /app
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
   pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload", "--port=80"]