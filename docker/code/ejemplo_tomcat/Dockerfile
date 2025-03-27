# Desplegar una aplicación java Web Din. en un servidor Tomcat
# El puerto se va a parametrizar desde la imagen

FROM tomcat

# Definir un argumento PORT:
ARG PORT=3000

# Exponer el puerto:
EXPOSE ${PORT}

# Definir el directorio de trabajo (indicamos la 
# carpeta de publicación de tomcat)
WORKDIR /usr/local/tomcat/webapps

# Copiar el fichero WAR al directorio de trabajo
COPY aplicacion1.war /usr/local/tomcat/webapps/ROOT.war

# Para generar la plantilla:
# docker build --build-arg PORT=8080 -t nombre_img .
# docker run -d --name tomcat1 -p 8080:8080 nombre_img
