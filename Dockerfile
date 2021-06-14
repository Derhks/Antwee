FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

RUN chmod u+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
