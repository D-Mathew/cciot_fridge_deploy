FROM ubuntu:18.04

# Update and install build dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    wget \
    build-essential \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    && apt-get clean

# Define Python version
ENV PYTHON_VERSION=3.9.9

# Download and build Python from source
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xvf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz

# Set Working Directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Dependencies
RUN pip install coqui-tts

# Expose the port the app listens on
EXPOSE 9002

# Command to run the app
CMD ["python3", "app.py"]

