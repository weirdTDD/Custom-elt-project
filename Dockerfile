FROM python:3.13.11-slim

RUN apt-get update && apt-get install -y postgresql-client

COPY elt/script.py .

CMD [ "python", "elt/script.py" ] 