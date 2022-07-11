from datetime import datetime
import email
from urllib import response
import requests
from lib.base_case import BaseCase
from lib.Assertions import Assertions


class TestUserRegister(BaseCase):

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_date(email)


        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists"
        print()
        print(response.status_code)
        print(response.content)

    def test_create_new_user_successfully(self):
        data = self.prepare_registration_date()

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_have_key(response, "id")