# Use the official Python image as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the main.py file and test files to the container
COPY main.py .
COPY test_compare.py .
COPY test_div_by3_6.py .
COPY test_multiplication.py .
COPY test_runner.py .
COPY test_square.py .
COPY test_string.py .

# Install pytest and any other dependencies
RUN pip install pytest

# Specify the command to run on container start
CMD ["pytest"]
