# Ejemplo para ejecutar una aplicación de python
FROM python:3.9-slim

# Establecer un directorio de trabajo
WORKDIR /aplicacion

# Copiar el fichero de Python:
COPY librerias.txt .
COPY codigo.py .

RUN pip install --no-cache-dir -r librerias.txt

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar el comando:
CMD ["python", "codigo.py"]
