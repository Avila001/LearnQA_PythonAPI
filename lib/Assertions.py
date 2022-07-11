from requests import JSONDecodeError, Response

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, key_name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Ответ не является JSON форматом. Текст ответа: '{response.text}'"

        assert key_name in response_as_dict, f"В JSON ответе нет ключа {key_name}"
        assert response_as_dict[key_name] == expected_value, error_message

    @staticmethod
    def assert_json_have_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Ответ не является JSON форматом. Текст ответа: '{response.text}'"

        assert name in response_as_dict, f"В JSON ответе нет ключа {name}"

    @staticmethod
    def assert_json_have_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Ответ не является JSON форматом. Текст ответа: '{response.text}'"

        assert name not in response_as_dict, f"В JSON ответе есть ключ {name}. Его быть не должно"

    @staticmethod
    def assert_json_have_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except JSONDecodeError:
            assert False, f"Ответ не является JSON форматом. Текст ответа: '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"В JSON ответе нет ключа {name}"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        response_as_dict = response.status_code
        assert expected_status_code == response_as_dict, f"Статус код не тот. Ожидаемый: {expected_status_code}. Пришедший: {response_as_dict}" 