FROM python:latest

RUN mkdir -p app

COPY . /application

WORKDIR /application

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python main.py