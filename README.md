# Changuito smart

Trabajo práctico para la materia Taller de programación III de la Facultad de Ingeniería de la UBA.

### Solución

La solución corre en containers de Docker y se encuentra arquitecturada con docker-compose. Adicionalmente fue
generado un makefile para facilitar el proceso de creación de imágenes y comienzo y fin de corrida de cada container.

#### Uso

Creación de las imagenes

    `make docker-image`

Levantar los containers

    `docker-compose-up`

Bajar los containers

    `docker-compose-down`


