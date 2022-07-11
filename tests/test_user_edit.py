from lib.base_case import BaseCase
from lib.Assertions import Assertions
import requests


class TestUserEdit(BaseCase):
    def test_user_edit(self):
        #REGISTER
        register_data = self.prepare_registration_date()
        response1 = requests.post(f"https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_have_key(response1, "id")

        #LOGIN
        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, 'id')

        login_data = {
            'email': email,
            'password': password
        }

        response2 = requests.post(f"https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        #EDIT
        new_name = "Changed Name"
        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data = {'firstName': new_name}
        )
        Assertions.assert_code_status(response3, 200)

        #GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        #print(response4.json()['firstName'])
        Assertions.assert_json_value_by_name(
            response4,
            'firstName',
            new_name,
            f"firstName не изменилось или другая ошибка. Ожидаемый firstName: {new_name}"
        )







