import unittest
from sender_stand_request import send_create_kit_request

class TestKitName(unittest.TestCase):

    def test_kit_name_min_length(self):
        # Prueba 1: Nombre con 1 carácter
        kit_body = {"name": "a"}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 201, f"Error: {response.status_code}, {response.json()}")
        self.assertEqual(response.json()["name"], "a", "El nombre no coincide con el solicitado.")
        print("Prueba 1 exitosa: El kit con un nombre de 1 carácter se creó correctamente.")

    def test_kit_name_511_characters(self):
        # Prueba 2: Nombre con 511 caracteres
        kit_body = {"name": "A" * 511}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 201, f"Error: {response.status_code}, {response.json()}")
        self.assertEqual(response.json()["name"], kit_body["name"], "El nombre no coincide con el solicitado.")
        print("Prueba 2 exitosa: El kit con un nombre de 511 caracteres se creó correctamente.")

    def test_kit_name_exceeds_max_length(self):
        # Prueba 3: Nombre con más de 512 caracteres (debe fallar)
        kit_body = {"name": "A" * 513}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 400, f"Error: Se esperaba 400, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        print("Prueba 3 exitosa: El kit con un nombre de más de 512 caracteres fue rechazado correctamente.")

    def test_kit_name_with_special_characters(self):
        # Prueba 4: Se permiten caracteres especiales
        kit_body = {"name": "№%@\", "}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 201, f"Error: Se esperaba 201, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        self.assertEqual(response.json()["name"], kit_body["name"], "El nombre no coincide con el solicitado.")
        print("Prueba 4 exitosa: El kit con un nombre que contiene caracteres especiales se creó correctamente.")

    def test_kit_name_with_spaces(self):
        # Prueba 5: Se permiten espacios en el nombre
        kit_body = {"name": " A Aaa "}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 201, f"Error: Se esperaba 201, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        self.assertEqual(response.json()["name"], kit_body["name"], "El nombre no coincide con el solicitado.")
        print("Prueba 5 exitosa: El kit con un nombre que contiene espacios se creó correctamente.")

    def test_kit_name_with_numbers(self):
        # Prueba 6: Se permiten números en el nombre
        kit_body = {"name": "123"}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 201, f"Error: Se esperaba 201, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        self.assertEqual(response.json()["name"], kit_body["name"], "El nombre no coincide con el solicitado.")
        print("Prueba 6 exitosa: El kit con un nombre que contiene números se creó correctamente.")

    def test_kit_name_missing(self):
        # Prueba 7: No se pasa el parámetro name (debe fallar)
        kit_body = {}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 400, f"Error: Se esperaba 400, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        print("Prueba 7 exitosa: La API rechazó correctamente la solicitud sin el parámetro name.")

    def test_kit_name_as_number(self):
        # Prueba 8: Se pasa un número en lugar de una cadena en el nombre (debe fallar)
        kit_body = {"name": 123}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 400, f"Error: Se esperaba 400, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        print("Prueba 8 exitosa: La API rechazó correctamente el nombre pasado como número.")

    def test_kit_name_empty(self):
        # Prueba 9: Nombre vacío (debe fallar)
        kit_body = {"name": ""}
        response = send_create_kit_request(kit_body)
        self.assertEqual(response.status_code, 400, f"Error: Se esperaba 400, pero se recibió {response.status_code}. Respuesta: {response.json()}")
        print("Prueba 9 exitosa: La API rechazó correctamente el nombre vacío.")

if __name__ == '__main__':
    unittest.main()


