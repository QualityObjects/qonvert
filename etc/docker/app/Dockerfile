FROM python:3.8-slim as builder

LABEL maintainer="Roberto Sánchez <rsanchez@qualityobjects.com>"
ENV TZ Europe/Madrid

RUN apt update 2>/dev/null && apt install -y --no-install-recommends curl gcc libc-dev linux-libc-dev \
      && python3 -m pip install --upgrade pip wheel \
      && apt clean && apt purge -y --auto-remove gcc libc-dev linux-libc-dev

ARG project_src=qonvert-src.tgz
ENV GENERATED_PACKAGE="qonvert.whl"

ENV WORKSPACE=/build/qonvert
RUN mkdir -p $WORKSPACE
WORKDIR "$WORKSPACE"

ADD $project_src $WORKSPACE

RUN cd $WORKSPACE && python setup.py bdist_wheel && cp dist/qonvert_server*.whl /build/$GENERATED_PACKAGE

FROM qualityobjects/asgi-server:latest as runner

ENV GENERATED_PACKAGE="qonvert.whl"

COPY --from=builder /build/$GENERATED_PACKAGE /tmp/
RUN python3 -m pip install -t /app /tmp/$GENERATED_PACKAGE
ENV PYTHONPATH /app
ENV WORKERS_PER_CORE 2
ENV WEB_CONCURRENCY 1
ENV HOST 0.0.0.0
ENV PORT 8080
ENV LOG_LEVEL info
ENV BIND "${HOST}:${PORT}"

ENV MODULE_NAME qonvert
ENV APP_NAME app
EXPOSE 8080

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start_app.sh"]


