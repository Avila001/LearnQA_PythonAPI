from urllib import response
import requests
from lib.Assertions import Assertions
from lib.base_case import BaseCase

class TestUserGet(BaseCase):
    def test_get_user_with_details_no_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")

        Assertions.assert_json_have_key(response, "username")    
        Assertions.assert_json_have_no_key(response, "email")

    def test_get_user_with_details_auth_with_same_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post(f"https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        need_params = ["username", "firstName", "lastName", "email"]

        Assertions.assert_json_have_keys(response2, need_params)



