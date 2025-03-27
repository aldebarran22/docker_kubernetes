# Crear una imagen basada en ubuntu para instalar y ejecutar
# el servidor nginx
FROM ubuntu:20.04

# Instalar dentro de Ubuntu el servidor nginx
RUN apt-get update && apt-get install -y nginx

# Establecer el directorio por defecto:
WORKDIR /var/www/html

# Copiar el fichero index.html a la carpeta de publicación:
COPY index.html .

# Exponer el puerto 80
EXPOSE 80

# Lanzar el servidor:
CMD ["nginx", "-g", "daemon off;"]

# docker build -t img_nginx .
# docker run --rm -d --name nginx1 -p 8008:80 img_nginx