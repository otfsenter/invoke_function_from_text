
class Context():
    def __init__(self):
        self.func_dict = {}

    def register_function(self, function):
        func_name = function.__name__
        self.func_dict.setdefault(func_name, function)

    def get(self, func_name):
        return self.func_dict.get(func_name)


