import json

from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Ошибка! Статус код не верный: {response.status_code}"
        print("Статус код верный: " + str(response.status_code))

    @staticmethod
    def check_json_response(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Ошибка! Обязательные поля не совпадают"
        print("Все обязательные поля совпадают")


    @staticmethod
    def check_data_response(response: Response, expected_keys):
        token = json.loads(response.text)
        data_objects = token.get('data', [])

        for item in data_objects:
            assert all(key in item for key in expected_keys), f"Ошибка! Обязательные поля пользователя " \
                                                              f"не совпадают: {response.text}"

        print("Все обязательные поля пользователя совпадают")