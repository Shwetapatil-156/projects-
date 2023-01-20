# Set base image (host OS)
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the project directory to the working directory
COPY . .

# Specify the Flask environment port
ENV PORT  8050

# By default, listen on port 5000
EXPOSE 8050

CMD gunicorn --bind 0.0.0.0:8050 app:server
