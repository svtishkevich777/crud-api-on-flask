FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "-w 4", "run:app"]
