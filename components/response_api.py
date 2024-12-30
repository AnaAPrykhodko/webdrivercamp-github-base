from jsonpath_ng import jsonpath, parse


class ResponseAPI():
    def __init__(self, response):
        self.status_code = response.status_code
        if response.text != "":
            self.json_data = response.json()

    def verify_status_code(self, value):
        assert self.status_code == int(value)


    def verify_length(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert len(match) == int(value)


    def verify_contains(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert value in match


    def verify_equals(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert str(match[0].value) == value
