class Upper_string:
    def __init__(self):
        self.string1 = ""

    def get_string(self, string1):
        self.string1 = string1

    def print_upper_string(self):
        print(self.string1.upper())

obj = Upper_string()
obj.get_string("пример")
obj.print_upper_string()

