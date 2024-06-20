class RequestStatus:
    def __init__(self):
        self.errors = {}
        self.data = {}

    def add_error(self, key, value):
        self.errors[key] = value

    def add_data(self, key, value):
        self.data[key] = value

    def is_empty(self):
        return len(self.errors) == 0