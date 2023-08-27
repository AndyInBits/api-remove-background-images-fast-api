FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt


CMD ["uvicorn", "app.main:app", "--port", "5000", "--reload"]