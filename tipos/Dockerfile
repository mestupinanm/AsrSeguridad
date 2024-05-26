FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the django app to the working directory
COPY . /app

# Set the environment tipos
ENV TIPOS_DB_HOST 10.128.0.82

# Install system dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev openssl-dev && \
    # Remove any existing Rust installation
    apk del cargo rust && \
    # Install Rust (Using rustup to manage Rust versions)
    curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    source $HOME/.cargo/env && \
    rustup default 1.63.0

# Update PATH to include cargo bin directory
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]
