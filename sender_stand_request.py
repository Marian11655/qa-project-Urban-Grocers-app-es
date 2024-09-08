# sender_stand_request.py
import requests
from configuration import URL_SERVICE, KITS_PATH, HEADERS
from data import auth_token

# Función para enviar una solicitud POST para crear un kit
def send_create_kit_request(kit_body):
    url = f"{URL_SERVICE}{KITS_PATH}"  # Construye la URL del servicio

    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {auth_token}"  # Añade el token de autorización

    # Realiza la solicitud POST con el kit_body recibido
    response = requests.post(url, headers=headers, json=kit_body)

    return response  # Retorna la respuesta del servidor
