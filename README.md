# Reto Captación

**Jon Cañadas, Iñigo Murga y Mikel García**

## Explicación

Este proyecto es un reto de captación de datos mediante MAGE y PostgreSQL. Incluye tres pasos diferentes: lectura, transformación y escritura de datos. Para la realización seguimos los siguientes pasos:

1. Diseño del docker-compose

Para el diseño del docker-compose hemos tenido en cuenta las características más importantes que hemos considerado, añadiendo alguna más para mejorar el uso de los servicios. 

2. Creación de una tabla en PostgreSQL

Tras construir y ejecutar los contenedores, accedemos a PostgreSQL con las credenciales específicas y basándonos en una base de datos de una tienda creamos una tabla e insertamos los datos pertinentes.

3. Captación en MAGE 

Una vez que tenemos la tabla con los datos, creamos un pipeline con tres etapas correspondiendo a la de lectura, transformación y escritura. En cada unas de las etapas introducimos el código requerido y lo ejecutamos, comprobando que en PostgreSQL se crea adecuadamente la tabla.

## Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/inigomurga/captacion-E1.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd captacion-E1
    ```
3. Construir y ejecutar los contenedores Docker:
    ```bash
    docker-compose up -d
    ```

## Uso

1. Abre la interfaz de Mage en tu navegador:
    ```markdown
    http://localhost:6789
    ```
2. Crea un nuevo pipeline y añade las etapas de lectura, transformación y escritura.
3. Ejecuta el pipeline y revisa los resultados en la base de datos PostgreSQL.

## Configuración de Docker Compose

Aquí está la configuración de Docker Compose para los servicios de Mage y PostgreSQL:

```yaml
services:
  mage:
    image: mageai/mageai:latest # Imagen de MAGE para Docker
    container_name: mage # Nombre del contenedor
    depends_on: # El servicio va a depender del contenedor que se especifique
      - postgres # Contenedor del que depende
    command: bash -c "pip install pandas sqlalchemy && mage start magic" # Ejecuta el comando especificado, en este caso instala una librería y arranca mage
    env_file: # Informa que hay un archivo de variables de entorno
      - .env # Archivo donde están las variables de entorno
    environment: # Especificar la variables de entorno
      ENV: dev # Entorno de desarrollo
      POSTGRES_DB: ${POSTGRES_DB} # Nombre de la base de datos
      POSTGRES_USER: ${POSTGRES_USER} # Usuario de la base de datos
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} # Contraseña de la base de datos
      POSTGRES_HOST: ${POSTGRES_HOST} # Host del PostgresSQL
      PG_HOST_PORT: ${PG_HOST_PORT} # Puerto del host de PostgresSQL
    ports: # Mapeo de puertos
      - 6789:6789 # Puertos específicos, el primero es en referencia al puerto local y el segundo al del contenedor de Docker
    volumes: # Volumen para la persistencia de datos
      - .:/home/src/ #Ubicación del volumen
    restart: always # Política de reinicio

  postgres:
    image: postgres:17 # Imagen de PostgresSQL para Docker
    restart: always # Política de reinicio
    container_name: postgres # Nombre del contenedor
    env_file: # Informa que hay un archivo de variables de entorno
      - .env # Archivo donde estan las variables de entorno
    environment: # Especificar la variables de entorno
      POSTGRES_DB: ${POSTGRES_DB} # Nombre de la base de datos
      POSTGRES_USER: ${POSTGRES_USER} # Usuario de la base de datos
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} # Contraseña de la base de datos
    ports: # Mapeo de puertos
      - "${PG_HOST_PORT}:5432" # Puertos específicos, el primero es en referencia al puerto local y el segundo al del contenedor de Docker

```

## Posibles vías de mejora

Para mejorar el reto hemos tomado una serie de decisiones a la hora de realizar el docker-compose:

* Utilizar un tag en la imagen de PostgresSQL, puesto que de esta forma aseguramos que los servicios funcionen evitando conflictos con futuras versiones. 
* La persistencia de los datos tanto en el servicio de PostgresSQL como en el de MAGE a través de los volúmenes especificados en el docker-compose.
* Incluir una política de reinicio mejora la fiabilidad y disponibilidad del servicio, reiniciandose en el caso de que el contenedor falle.


## Problemas / Retos encontrados

Durante el reto hemos tenido problemas con el flujo de código entre los integrantes, esto se ha generado por estar poco acostumbrados al uso de git. Por lo que, esperamos ir mejorando mientras avanzamos en la asignatura.

A su vez, el hecho de estar continuamente metiendo los datos tanto en postgres como en mage se nos hizo pesado, encontrando la mejora de persistencia de datos que nos ha ahorrado bastante tiempo.

## Alternativas posibles

Implementar algún servicio de seguridad, puesto que cualquiera puede acceder a los servicios.
