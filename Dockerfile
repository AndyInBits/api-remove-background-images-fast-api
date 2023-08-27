FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt


CMD ["uvicorn", "main:app", "--port", "5000", "--reload", "--host", "0.0.0.0"]