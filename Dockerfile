FROM python:3.12 as base
WORKDIR /code

FROM base as dev
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

FROM base as prod
COPY ./requirements-prod.txt /code/requirements-prod.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements-prod.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
