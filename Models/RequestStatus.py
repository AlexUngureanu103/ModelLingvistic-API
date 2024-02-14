class RequestStatus:
    def __init__(self):
        self.errors = {}

    def add_error(self, key, value):
        self.errors[key] = value

    def is_empty(self):
        return len(self.errors) == 0