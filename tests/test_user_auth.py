import requests
import pytest
from lib.base_case import BaseCase
from lib.Assertions import Assertions

class TestUserAuth(BaseCase):
    negative_data = {
            ("no_cookies"),
            ("no_token")
        }

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(response, 'auth_sid')
        self.token = self.get_header(response, 'x-csrf-token')
        self.user_id_from_auth_metod = self.get_json_value(response, "user_id")

    def test_auth_user(self):        
        response2 = requests.get("https://playground.learnqa.ru/api/user/auth", headers={'x-csrf-token': self.token},
                                 cookies={'auth_sid': self.auth_sid})

        Assertions.assert_json_value_by_name(
            response2,
            'user_id',
            self.user_id_from_auth_metod,
            "Полученное значение ключа 'user_id' не совпадает c ожидаемым (отправленным при создании пользователя)"
        )
        # self.expected_user_id = response2.json()["user_id"]
        # assert 'user_id' in response2.json(), "нет user_id"
        # assert self.expected_user_id == self.user_id, "user_id не совпадают"

    
    @pytest.mark.parametrize('negative', negative_data)
    def test_negative_auth(self, negative):
        if negative == 'no_cookies':
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth", 
                headers={'x-csrf-token': self.token})
        else: 
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={'auth_sid': self.auth_sid}
            )

        expected_id = response2.json()['user_id']
        assert expected_id == 0, 'Ошибка негативного теста'
