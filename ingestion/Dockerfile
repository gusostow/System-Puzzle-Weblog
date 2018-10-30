FROM python:3.7

RUN mkdir /usr/src/ingestion
WORKDIR /usr/src/ingestion
RUN mkdir weblogs
COPY . .
RUN pip install -r requirements_ingestion.txt

CMD ["python", "ingestion.py"]
