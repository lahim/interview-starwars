FROM python:3.8-slim

RUN apt-get update && mkdir -p /app/backend/

WORKDIR /app/backend/

COPY . .

RUN pip install --upgrade pip wheel && \
    pip install -r requirements.txt

VOLUME /app/backend/

EXPOSE 8000

CMD ['bash', 'run.sh']
