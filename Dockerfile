###########
# Builder #
###########

# Set the base image for build stage
FROM python:3.12-slim as builder

# Set the working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    musl-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN pip install --upgrade pip

# Install dependencies 
# First copy only the requirements file to leverage Docker cache
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# Final #
#########

# Set the base image for final stage
FROM python:3.12-slim

# Create a directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN addgroup --system app && adduser --system --group app

# Create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME

# Set environment variables
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies by copying the wheels from the builder stage
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# Copy entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# Copy project
COPY . $APP_HOME

# Set django settings module
ENV DJANGO_SETTINGS_MODULE=core.settings

# Chawn all the files to the app user
RUN chown -R app:app $APP_HOME

# Change to the app user
USER app

# Run the entrypoint
# I'll run it in the docker-compose file from now on
# ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]







