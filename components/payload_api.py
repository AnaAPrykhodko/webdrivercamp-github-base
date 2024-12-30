import json
# Add methods:
#
# That reads the payload from a file
#
# That updates the payload ( add / delete / replace a value by key using JSONPath)
class PayloadAPI():
    def __init__(self, filename=None):
        if filename is not None:
            with open(filename, 'r') as json_file:
                self.json_data = json.load(json_file)


    def add(self, value):
        self.json_data = value

    def replace(self, value):
        pass


    def to_file(self, filename):
        with open(filename, 'w') as writer:
            writer.write(json.dumps(self.json_data))


    def to_json(self):
        return json.dumps(self.json_data)