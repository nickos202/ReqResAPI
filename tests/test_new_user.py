from func.api_reqres import ReqResApi
from func.cheking import Checking


class Test_new_user:

    def test_create_user(self):
        print("Метод POST - Create")
        result_create_user = ReqResApi.create_user()
        Checking.check_status_code(result_create_user, 201)
        Checking.check_json_response(result_create_user, ['name', 'job', 'id', 'createdAt'])

        print("Метод PUT - Update")
        result_update_user = ReqResApi.update_user()
        Checking.check_status_code(result_update_user, 200)
        Checking.check_json_response(result_update_user, ['name', 'job', 'updatedAt'])
        Checking.check_json_value(result_update_user, 'job', 'zion resident')

        print("Метод DELETE - Delete")
        result_delete_user = ReqResApi.delete_user()
        Checking.check_status_code(result_delete_user, 204)