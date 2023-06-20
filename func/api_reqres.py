from func.methods import Methods
base_url = "https://reqres.in" # базовая URL


class ReqResApi:

    @staticmethod
    def get_list_users_page_2():
        """Метод просмотра списка пользователей"""

        list_users_resource = "/api/users" # Resource списка пользователей
        key = "?page=2"
        get_list_users_url = base_url + list_users_resource + key
        print(get_list_users_url)
        result_get_list_users = Methods.get(get_list_users_url)
        return result_get_list_users

    @staticmethod
    def get_single_user():
        """Метод просмотра информации о пользователе"""

        single_user_resource = "/api/users/2"
        get_single_user_url = base_url + single_user_resource
        print(get_single_user_url)
        result_get_single_user = Methods.get(get_single_user_url)
        return result_get_single_user

    @staticmethod
    def get_single_user_not_found():
        """Метод просмотра информации о несуществующем пользователе"""

        single_user_not_found_resource = "/api/users/23"
        get_single_user_not_found_url = base_url + single_user_not_found_resource
        print(get_single_user_not_found_url)
        result_get_single_user_not_found = Methods.get(get_single_user_not_found_url)
        return result_get_single_user_not_found