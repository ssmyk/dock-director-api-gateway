FROM python:3.12-alpine

WORKDIR dock_director_api_gateway
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY app/ app/
CMD ["pipenv", "run", "app/main.py"]
