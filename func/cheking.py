import json

from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Ошибка! Статус код не верный: {response.status_code}"
        print("Статус код верный: " + str(response.status_code))


    """"Методы проверки списка пользователей"""

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
        print("Обязательные поля пользователя совпадают")


    """"Методы проверки информации о пользователе"""

    @staticmethod
    def check_info_single_user(response: Response, expected_keys):
        token = json.loads(response.text)
        data_object = token.get('data', {})
        data_keys = set(data_object.keys())
        assert data_keys == expected_keys, f"Ошибка! Обязательные поля информации о пользователе" \
                                           f" отсутствуют: {response.text}"
        print("Обязательные поля пользователя совпадают")

    @staticmethod
    def check_json_value(response: Response, fild_name, expected_value):
        check = response.json()
        check_info = check.get(fild_name)
        assert check_info == expected_value, f"Содержимое поля {fild_name} неверное: {check_info}"
        print(f"Содержимое поля {fild_name} верное: {check_info}")