# Ejemplo para ejecutar una aplicación de python
FROM python:3.9-slim

# Establecer un directorio de trabajo
WORKDIR /aplicacion

# Copiar el fichero de Python:
COPY librerias.txt .
COPY app.py .

RUN pip install --no-cache-dir -r librerias.txt

# Exponer el puerto 5001
EXPOSE 5001

# Ejecutar el comando:
CMD ["python", "app.py"]
