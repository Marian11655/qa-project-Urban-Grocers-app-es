# Proyecto: Urban Grocers - API Testing

## Descripción del Proyecto

Este proyecto tiene como objetivo realizar pruebas automatizadas sobre una API que permite la creación de kits de productos para usuarios o tarjetas en la aplicación **Urban Grocers**. Las pruebas están enfocadas en validar la correcta creación de kits bajo diferentes escenarios y validaciones del campo `name` (nombre del kit).

### Funcionalidades clave:
- Creación de kits a través de la API usando el método `POST`.
- Verificación de respuestas de la API para diferentes escenarios de longitud de caracteres en el campo `name`.
- Validaciones de campos obligatorios y restricciones de la API, como la longitud mínima y máxima permitida.
- Manejo de errores, como la falta de parámetros obligatorios o valores no válidos.

## Estructura del Proyecto

- **`configuration.py`**: Contiene la configuración del proyecto, incluyendo la URL base de la API y las rutas para crear usuarios y kits.
  
- **`data.py`**: Almacena los datos necesarios para las pruebas, como el token de autenticación (`auth_token`) y el nombre del kit.

- **`sender_stand_request.py`**: Este archivo maneja las solicitudes a la API. Implementa la lógica para realizar solicitudes `POST` para la creación de kits, utilizando los datos de `data.py`.

- **`create_kit_name_kit_test.py`**: Contiene las pruebas automatizadas para validar la creación de kits. Se incluyen diferentes casos de prueba para verificar la correcta validación del campo `name`, incluyendo la longitud mínima, máxima, y casos límite.

## Pruebas Implementadas

Las siguientes pruebas automatizadas están diseñadas para validar la longitud del campo `name` en la creación de kits:

| Nº  | Descripción                                                                                     | Respuesta esperada (ER)                                                                                                                                                       |
| --- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | El número permitido de caracteres (1): `kit_body = {"name": "a"}`                                 | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.                                                  |
| 2   | El número permitido de caracteres (511): `kit_body = {"name": "El valor de prueba será inferior a"}` | Código de respuesta: 201. El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud.                                              |
| 3   | El número de caracteres es menor que la cantidad permitida (0): `kit_body = {"name": ""}`         | Código de respuesta: 400.                                                                                                                                                     |
| 4   | El número de caracteres es mayor que la cantidad permitida (512): `kit_body = {"name": "El valor de prueba será inferior a..."}` | Código de respuesta: 400.                                                                                             |
| 5   | La solicitud sin el campo `name`: `kit_body = {}`                                                 | Código de respuesta: 400.                                                                                                                                                     |
| 6   | El campo `name` contiene solo caracteres numéricos: `kit_body = {"name": "123456"}`               | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.                                                  |
| 7   | El campo `name` contiene una mezcla de caracteres alfanuméricos: `kit_body = {"name": "Kit123"}`  | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.                                                  |
| 8   | El campo `name` contiene caracteres especiales permitidos: `kit_body = {"name": "@Kit_#2024"}`    | Código de respuesta: 201. El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.                                                  |
| 9   | El campo `name` contiene caracteres no permitidos: `kit_body = {"name": "Kit<>¿?!"}`              | Código de respuesta: 400.                                                                                                                                                     |

## Requisitos

- **Python 3.12+**
- **Librerías**:
  - `requests`: Se utiliza para manejar las solicitudes HTTP a la API.
  
  Instalar con:

  ```bash
  pip install requests
