FROM python:3.7

RUN mkdir /usr/src/ingestion
WORKDIR /usr/src/ingestion
COPY . .
RUN pip install -r requirements_ingestion.txt
EXPOSE 5672

CMD ["python", "ingestion.py"]
