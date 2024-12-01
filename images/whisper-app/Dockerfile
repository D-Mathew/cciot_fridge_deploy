FROM python:3.12-slim

RUN apt update && apt install -y curl && apt install -y ffmpeg && apt clean

# Set Working Directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Port the app listens on
EXPOSE 9001

# Command to run the app
CMD ["python", "app.py"]
