from func.methods import Methods
base_url = "https://reqres.in" # базовая URL
mock_url = "http://localhost:3000"


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

    @staticmethod
    def create_user():
        """Метод создания пользователя"""

        create_resource = "/api/users"
        json_create = {
            "name": "morpheus",
            "job": "leader"
        }
        create_url = base_url + create_resource
        print(create_url)
        result_create = Methods.post(create_url, json_create)
        return result_create

    @staticmethod
    def update_user():
        """Метод изменения данных пользователя"""

        update_resource = "/api/users/2"
        json_update = {
            "name": "morpheus",
            "job": "zion resident"
        }
        update_url = base_url + update_resource
        print(update_url)
        result_update = Methods.put(update_url, json_update)
        return result_update

    @staticmethod
    def delete_user():
        """Метод удаления пользователя"""

        delete_resource = "/api/users/2"
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Methods.delete(delete_url)
        return result_delete


class Mockoon(ReqResApi):


    @staticmethod
    def post_register_successful():

        """Метод регистрации нового пользователя c использованием Mock сервера"""

        register_resource = "/api/register"
        json_register = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        register_url = mock_url + register_resource
        print(register_url)
        result_post_register = Methods.post(register_url, json_register)
        return result_post_register

    @staticmethod
    def post_register_unsuccessful():

        """Метод регистрации нового пользователя c использованием Mock сервера - негативная проверка"""

        register_resource = "/api/register"
        json_register = {
            "email": "eve.holt@reqres.in"
        }
        register_url = mock_url + register_resource
        print(register_url)
        result_post_register = Methods.post(register_url, json_register)
        return result_post_register

    @staticmethod
    def post_login_successful():

        """Метод авторизации пользователя c использованием Mock сервера"""

        login_resource = "/api/login"
        json_login = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        login_url = mock_url + login_resource
        print(login_url)
        result_post_login = Methods.post(login_url, json_login)
        return result_post_login

    @staticmethod
    def post_login_unsuccessful():

        """Метод авторизации пользователя c использованием Mock сервера - негативная проверка"""

        login_resource = "/api/login"
        json_login = {
            "email": "eve.holt@reqres.in"
        }
        login_url = mock_url + login_resource
        print(login_url)
        result_post_login = Methods.post(login_url, json_login)
        return result_post_login