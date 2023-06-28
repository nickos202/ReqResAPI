from func.api_reqres import Mockoon
from func.cheking import Checking


class TestRegisterUserMock:


    def test_register_user_mock(self):
        print("Метод POST REGISTER-SUCCESSFUL Mockoon")
        result_post_register = Mockoon.post_register()
        Checking.check_status_code(result_post_register, 200)
        Checking.check_json_register_mock(result_post_register, ['id', 'token'])

    def test_register_user_mock_unsuccessful(self):
        print("Метод POST REGISTER-UNSUCCESSFUL Mockoon")
        result_post_register_unsuccessful = Mockoon.post_register_unsuccessful()
        Checking.check_status_code(result_post_register_unsuccessful, 400)
        Checking.check_json_value(result_post_register_unsuccessful, 'error', 'Missing password')

    def test_login_user_mock(self):
        print("Метод POST LOGIN-SUCCESSFUL Mockoon")
        result_post_login = Mockoon.post_login_successful()
        Checking.check_status_code(result_post_login, 200)
        Checking.check_json_register_mock(result_post_login, ['token'])

    def test_login_user_mock_unsuccessful(self):
        print("Метод POST LOGIN-UNSUCCESSFUL Mockoon")
        result_post_login_unsuccessful = Mockoon.post_login_unsuccessful()
        Checking.check_status_code(result_post_login_unsuccessful, 400)
        Checking.check_json_value(result_post_login_unsuccessful, 'error', 'Missing password')