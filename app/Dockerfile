# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app/ /app

# Copy SSL certificates into the container
COPY app/certs/ /app/certs

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application with SSL
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]