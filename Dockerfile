FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./app /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh","/app/entrypoint.sh"]