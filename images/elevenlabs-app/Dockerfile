FROM python:3.12-slim

RUN apt update && apt install -y curl && install -y ffmpeg && apt clean 

# Set Working Directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app listens on
EXPOSE 9002

# Command to run the app
CMD ["python", "app.py"]

