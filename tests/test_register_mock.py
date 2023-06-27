from func.api_reqres import Mockoon
from func.cheking import Checking


class TestRegisterUserMock:


    def test_register_user_mock(self):
        print("Метод POST REGISTER-SUCCESSFUL Mockoon")
        result_post_register = Mockoon.post_register()
        Checking.check_status_code(result_post_register, 200)
        Checking.check_json_register_mock(result_post_register, ['id', 'token'])