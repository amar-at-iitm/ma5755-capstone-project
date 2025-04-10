# Dockerfile

FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Default command (you can override this in docker-compose)
CMD ["python", "scripts/data_download.py"]
