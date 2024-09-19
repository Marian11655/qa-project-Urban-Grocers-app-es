import unittest
from sender_stand_request import send_create_kit_request
import data

class TestKitName(unittest.TestCase):

    def positive_assert(self, kit_body):
        response = send_create_kit_request(kit_body)
        try:
            response_json = response.json()
        except ValueError:
            self.fail(f"Error: Respuesta no es JSON válida. Status code: {response.status_code}, Respuesta: {response.text}")
        self.assertEqual(response.status_code, 201, f"Error: {response.status_code}, {response.text}")
        self.assertEqual(response_json["name"], kit_body["name"], "El nombre no coincide con el solicitado.")

    def negative_assert(self, kit_body):
        response = send_create_kit_request(kit_body)
        try:
            response_json = response.json()
        except ValueError:
            self.fail(f"Error: Respuesta no es JSON válida. Status code: {response.status_code}, Respuesta: {response.text}")
        self.assertEqual(response.status_code, 400, f"Error: Se esperaba 400, pero se recibió {response.status_code}. Respuesta: {response.text}")

    def test_kit_name_min_length(self):
        self.positive_assert(data.one_letter)

    def test_kit_name_511_characters(self):
        self.positive_assert(data.max_length)

    def test_kit_name_exceeds_max_length(self):
        self.negative_assert(data.exceeds_max_length)

    def test_kit_name_with_special_characters(self):
        self.positive_assert(data.special_characters)

    def test_kit_name_with_spaces(self):
        self.positive_assert(data.spaces_in_name)

    def test_kit_name_with_numbers(self):
        self.positive_assert(data.numbers_in_name)

    def test_kit_name_missing(self):
        self.negative_assert(data.missing_name)

    def test_kit_name_as_number(self):
        self.negative_assert(data.name_as_number)

    def test_kit_name_empty(self):
        self.negative_assert(data.empty_name)

if __name__ == '__main__':
    unittest.main()




