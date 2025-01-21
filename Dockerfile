# Verwende ein leichtes Python-Image
FROM python:3.9-slim

# Setze den Arbeitsordner im Container
WORKDIR /app

# Kopiere die Dateien aus deinem Ordner in den Container
COPY . .

# Definiere den Befehl, der ausgeführt wird
CMD ["python", "hello.py"]
