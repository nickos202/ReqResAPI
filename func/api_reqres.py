from func.methods import Methods
base_url = "https://reqres.in" # базовая URL


class ReqResApi:

    @staticmethod
    def list_users_page_2():
        """Метод просмотра списка пользователей"""

        list_users_resource = "/api/users" # Resource списка пользователей
        key = "?page=2"
        get_list_users_url = base_url + list_users_resource + key
        print(get_list_users_url)
        result_get_list_users_url = Methods.get(get_list_users_url)
        return result_get_list_users_url