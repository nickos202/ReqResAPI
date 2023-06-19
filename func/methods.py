import requests as requests


class Methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result_get = requests.get(url, headers=Methods.headers, cookies=Methods.cookie)
        return result_get

    @staticmethod
    def post(url, body):
        result_post = requests.post(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        return result_post

    @staticmethod
    def put(url, body):
        result_put = requests.put(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        return result_put

    @staticmethod
    def delete(url, body):
        result_delete = requests.delete(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        return result_delete

    @staticmethod
    def patch(url, body):
        result_patch = requests.patch(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        return result_patch
    