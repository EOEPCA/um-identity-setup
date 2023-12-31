# run keycloak-setup to configure Keycloak
FROM python:alpine
RUN apk add --no-cache git
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "src/main.py"]
