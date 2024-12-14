FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# . en este caso es el WORKDIR, es decir /app
COPY requirements.txt .

# Install system dependencies for Alpine
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    python3-dev \
    libffi-dev \
    pkgconfig

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todos los files del host application al WORKDIR del container
COPY . .

RUN chmod +x ./entrypoint.sh

# No es necesario realmente
EXPOSE 8000