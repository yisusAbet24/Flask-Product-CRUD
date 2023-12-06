# CRUD Python Flask

Este proyecto implementa un CRUD básico de productos utilizando Python Flask.

## Instalación

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio en tu máquina local: 
   `git clone https://github.com/yisusAbet24/Flask-Product-CRUD.git`
2. instalar las dependencias.
3. Cambia la variable MONGO_URI en el archivo db.py con la conexión a tu base de datos MongoDB.
4. Inicia la aplicación con el siguiente comando:
   `python app.py`

## Uso

Este CRUD ofrece cuatro rutas principales: post, get, update, y delete.

## Modelo de Producto

```json
{
  "name": "Nombre del producto",
  "price": "Precio del producto",
  "quantity": "Cantidad disponible en stock"
}
```
