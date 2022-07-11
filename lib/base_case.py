import json
from requests import Response
import requests
from datetime import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не нашли куки с именем {cookie_name} в нашем запросе"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Не нашли заголовок {headers_name} в нашем запросе"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ не в JSON формате. Текст ответа: {response.text}"
        assert name in response_as_dict, f"Ответ JSON не имеет ключа {name}"
        return response_as_dict[name]

    def prepare_registration_date(self, email=None):
        if email is None:
            base_part = 'learnqa'
            domain = 'example.com'
            random_part = datetime.now().strftime("%d%m%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '1234',
            'email': email,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'username': 'learnqa'
        }


