# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variables
# ENV FLASK_APP=main.py
# ENV FLASK_RUN_PORT=5000

# Make port 8080 available to the world outside this container
EXPOSE 8080

ENTRYPOINT [ "python3" ]

# Run the Flask application
CMD ["main.py"]
