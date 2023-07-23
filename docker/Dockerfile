FROM python:3.6

RUN mkdir -p app

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python main.py