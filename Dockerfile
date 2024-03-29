FROM python:3.10-slim

RUN apt-get update && apt-get install -y cron

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install -e .

RUN echo "*/3 * * * * cd /app && /usr/local/bin/python3 manage.py update_cars_location" | crontab -

CMD ["cron", "-f"]
