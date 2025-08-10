# Start from a Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install build-essential for any C extensions that might be needed during pip install
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
# Using --no-cache-dir to reduce image size
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app /app/app

# Expose the port that the application will run on
EXPOSE 8000

# The command to run the application
# Uvicorn will be run by the docker-compose command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
