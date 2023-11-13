FROM python:3.12.0-slim
LABEL org.opencontainers.image.name=europe-west3-docker.pkg.dev/zeitonline-engineering/docker-zon/deployment-notify
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --no-deps -r requirements.txt

COPY pyproject.toml *.rst ./
COPY src src
RUN pip install --no-cache-dir -e . && pip check

ENTRYPOINT ["python", "-m", "deployment_notify"]
