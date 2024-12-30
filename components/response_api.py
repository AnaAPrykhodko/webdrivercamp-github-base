from jsonpath_ng import jsonpath, parse


class ResponseAPI():
    def __init__(self, response):
        self.status_code = response.status_code
        self.json_data = response.json()

    def verify_status_code(self, value):
        assert self.status_code == value


    def verify_length(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert len(match) == value


    def verify_contains(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert value in match


    def verify_equals(self, json_path, value):
        jsonpath_expression = parse(json_path)
        match = jsonpath_expression.find(self.json_data)
        assert match == value
