FROM python:3.12
WORKDIR /app
COPY . /app
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=product_catalog.settings
RUN ls -la
CMD ["sh", "-c", "sleep 10 && poetry run python manage.py migrate && poetry run python manage.py collectstatic --noinput && poetry run gunicorn product_catalog.wsgi:application -b 0.0.0.0:8000"]
