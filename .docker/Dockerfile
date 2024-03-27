FROM python:3.12-alpine
WORKDIR dock_director_api_gateway/
ENV PYTHONPATH=/dock_director_api_gateway
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY app/ app/
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
