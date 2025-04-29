# hadolint global ignore=DL3008
FROM debian:12-slim AS build 

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes \
    python3-venv gcc libpython3-dev libjpeg-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

FROM build AS build-venv

COPY requirements.txt /requirements.txt

RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt

FROM gcr.io/distroless/python3-debian12:latest-amd64

COPY --from=build-venv /venv /venv

WORKDIR /app
COPY . .

EXPOSE 8080

CMD ["/venv/bin/gunicorn", "--bind", "0.0.0.0:8080", "Project.wsgi:application"]
