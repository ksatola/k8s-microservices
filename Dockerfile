# Base image
#FROM python:latest
FROM python:3

# Set a directory for the app
#WORKDIR /usr/src/app
#WORKDIR /root/src

# Copy all the files to the container
#COPY /src .
#COPY /src/recommendations/requirements.txt .

# Install dependencies
#RUN pwd
#RUN pip install --no-cache-dir -r recommendations/requirements.txt

# Tell the port number the container should expose (the app is working on this port)
#EXPOSE 5000

# Run the command
# python ./app.py
#CMD ["python", "./app.py"]
