# hadolint global ignore=DL3008
FROM debian:12-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes \
    python3-venv gcc libpython3-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m venv /venv && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | /venv/bin/python && \
    /venv/bin/pip install --disable-pip-version-check -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3-debian12:latest-amd64

COPY --from=build /venv /venv
COPY --from=build /app /app

WORKDIR /app

EXPOSE 8080


CMD ["/venv/bin/python", "apps.py"]
