auth_token = "jknnFApafP4awfAIFfafam2fma"  # Token de autorización disponible en el API
kit_name = "Kit de Marian"  # El nombre del kit que estás creando
card_id = None  # cardId, vacio.
# Datos de prueba para las pruebas positivas
one_letter = {"name": "a"}
max_length = {"name": "A" * 511}
special_characters = {"name": "№%@\", "}
spaces_in_name = {"name": " A Aaa "}
numbers_in_name = {"name": "123"}

# Datos de prueba para las pruebas negativas
exceeds_max_length = {"name": "A" * 513}
missing_name = {}
name_as_number = {"name": 123}
empty_name = {"name": ""}