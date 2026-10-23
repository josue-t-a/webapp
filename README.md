
# backend application

## descripción general
> El proyecto consiste en crear una API REST básica escrita en fastAPI para interactuar con la tabla item

## workflow git
> el flujo de trabajo seguido es un GitFlow donde las ramas principales son *develop* y *main*. los cambios iniciales se realizaron de manera secuencial en ramas *feature*  a partir de *develop* usando el comando `git ckeckout -b feature/descr-corta` y se integraron a *develop* de forma transparente mediante merge locales con los comandos `git checkout develop` y `git checkout merge feature/descr-corta`.

> Cuando empezaron los cambios colaborativos se trabajó en ramas *feature* con cambios integrados mediante [pull request](https://github.com/josue-t-a/webapp/pulls) en el repositorio.

> Para la integración a main, una vez terminado el MVP, se creó una rama release donde se documentó este archivo con el comando `git checkout -b release/x.x.x` y posteriormente se integró a *main* y *develop* mediante PR.


## release/0.1.0

La solución integra los endpoints **/items** con el CRUD para interactuar con items. La documentación pueden encontrarse levantando el servidor local con el comando

`uv run fastapi dev`

en el localhost:8000/docs

## Uso
> fastAPI permite interactuar con la solución desde el endpoint /docs, pero se puede realizar mediante la conocida herramienta curl 

### crear un nuevo item

```
curl -X 'POST' \
  'http://localhost:8000/items' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "query": "item de prueba"
}'
```
### consultar todos los items
```
curl -X 'GET' \
  'http://localhost:8000/items' \
  -H 'accept: application/json'
```

### consultar un item por su id
```
curl -X 'GET' \
  'http://localhost:8000/items/0' \
  -H 'accept: application/json'
```