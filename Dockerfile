
FROM python:3.8-slim


WORKDIR /app


COPY . /app


CMD ["python", "-u", "counting_script.py"]