import requests as requests
from func.logger import Logger


class Methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result_get = requests.get(url, headers=Methods.headers, cookies=Methods.cookie)
        Logger.add_response(result_get)
        return result_get

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        result_post = requests.post(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        Logger.add_response(result_post)
        return result_post

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        result_put = requests.put(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        Logger.add_response(result_put)
        return result_put

    @staticmethod
    def delete(url):
        Logger.add_request(url, method="DELETE")
        result_delete = requests.delete(url, headers=Methods.headers, cookies=Methods.cookie)
        Logger.add_response(result_delete)
        return result_delete

    @staticmethod
    def patch(url, body):
        Logger.add_request(url, method="PATCH")
        result_patch = requests.patch(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        Logger.add_response(result_patch)
        return result_patch
    