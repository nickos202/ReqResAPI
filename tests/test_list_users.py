import json

from func.api_reqres import ReqResApi
from func.cheking import Checking


class Test_list_users:

    def test_list_users(self):
        print("Метод GET - List Users")
        result_get_list_users = ReqResApi.list_users_page_2()
        Checking.check_status_code(result_get_list_users, 200)
        Checking.check_json_response(result_get_list_users, ['page', 'per_page', 'total', 'total_pages',
                                                             'data', 'support'])
        Checking.check_data_response(result_get_list_users, ['id', 'email', 'first_name', 'last_name', 'avatar'])