FROM python:3.5

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3.5 manager.py runserver"]
