FROM python:latest

RUN mkdir -p home

COPY . /home

WORKDIR /home

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python main.py

COPY wait-for-it.sh /home

RUN chmod +x wait-for-it.sh