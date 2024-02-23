FROM python:3.9

# Set the working directory of the container to /app
WORKDIR /app

# Copy requirements file to /app
COPY requirements.txt /app

# Install dependencies using pip
RUN pip install -r /app/requirements.txt

# Copy rest of files to /app
COPY . /app

# Expose ports
EXPOSE 80

# Run the server
ENTRYPOINT ["python", "/app/server.py"]
