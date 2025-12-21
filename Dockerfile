FROM python:3.13.0-alpine3.20
WORKDIR /app
COPY sum.py /app/
CMD ["tail", "-f", "/dev/null"]
