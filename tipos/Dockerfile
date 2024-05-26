FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment tipos
ENV TIPOS_DB_HOST 10.128.0.82

# Install system dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev \
    libffi-dev openssl-dev cargo

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]
