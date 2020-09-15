FROM python:3.8-slim

LABEL maintainer="Roberto Sánchez <rsanchez@qualityobjects.com>"
ENV TZ Europe/Madrid

RUN apt update 2>/dev/null && apt install -y --no-install-recommends curl gcc libc-dev linux-libc-dev \
      && python3 -m pip install --upgrade pip uvicorn gunicorn \
      && apt clean && apt purge -y --auto-remove gcc libc-dev linux-libc-dev

COPY ./start_app.sh /start_app.sh
RUN chmod +x /start_app.sh

RUN mkdir -p /app /server_conf
COPY ./gunicorn_conf.py /server_conf/gunicorn_conf.py

WORKDIR /app/

VOLUME [ "/app", "/server_conf" ]

ENV PYTHONPATH /app
ENV WORKERS_PER_CORE 2
ENV WEB_CONCURRENCY 1
ENV HOST 0.0.0.0
ENV PORT 8080
ENV LOG_LEVEL info
ENV BIND "${HOST}:${PORT}"

ENV MODULE_NAME main
ENV APP_NAME app
EXPOSE 8080

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start_app.sh"]


