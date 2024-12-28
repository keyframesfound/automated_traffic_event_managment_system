# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Expose port 4000 for the Flask app
EXPOSE 4000

# Define environment variable
ENV FLASK_APP=Main.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=4000"]