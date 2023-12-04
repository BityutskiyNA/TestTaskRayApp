# Use the official Python image as a base image
FROM python:3.12-alpine as builder

# Set the working directory in the container
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for building Python packages
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Upgrade pip and install flake8
RUN pip install --upgrade pip --no-cache-dir \
    && pip install flake8==3.9.2

# Copy the local directory to the container
COPY . .


# Copy the poetry files
COPY pyproject.toml poetry.lock /usr/src/app/

# Install project dependencies
RUN pip install poetry \
    && poetry install --no-root --no-dev

# Export requirements and create wheels
RUN poetry export --format=requirements.txt --output=requirements.txt && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# Build the final image
FROM python:3.12-alpine

# Create and set the working directory
RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# Install libpq
RUN apk update && apk add libpq

# Copy wheels from the builder stage
COPY --from=builder /usr/src/app/wheels /wheels

# Install project dependencies from wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copy the entrypoint script
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.prod.sh
RUN chmod +x $APP_HOME/entrypoint.prod.sh

# Copy the rest of the application code
COPY . $APP_HOME

# Change ownership
RUN chown -R app:app $APP_HOME

# Set the user to run the application
USER app

# Set the entrypoint command
ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]
