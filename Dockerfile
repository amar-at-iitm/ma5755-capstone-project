# Dockerfile
FROM python:3.11-bullseye

#FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the rest of the project
COPY . .

# Leave CMD to be overridden by docker-compose
