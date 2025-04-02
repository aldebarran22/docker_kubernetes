# Imagen base:
FROM ubuntu

# Actualizar el sistema
RUN apt-get update

# Instalar apache
RUN apt-get install -y apache2 

# Copiar la carpeta Web al directorio de publicación:
ADD web /var/www/html

# Exponer el puerto
EXPOSE 80

# Arrancamos apache
CMD ["/usr/sbin/apachectl","-D","FOREGROUND"]
