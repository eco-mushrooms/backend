FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip nginx
RUN apt-get update && apt-get install -y python3  python3-pip nginx
# Set the working directory in the container
WORKDIR /app

# Copy the Django application code to the container
COPY . .

# convert all shell script to executable
RUN chmod +x *.sh

# Build wheel packages
RUN pip install -r requirements.txt
# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/sites-available/default

RUN mkdir -p /app/static

# Lets list the files
RUN ls -la


CMD ["/app/docker-entrypoint.sh"]
EXPOSE 80