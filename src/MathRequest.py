class MathRequest:

    def __init__ (self, ope1, operator, ope2):
        self.result = None
        self.ope1 = ope1
        self.operator = operator
        self.ope2 = ope2

    def get_ope1(self):
        return self.ope1

    def get_operator(self):
        return self.operator

    def get_ope2(self):
        return self.ope2

    def get_res(self, result = None):
        if result is not None:
            self.result = result
        return self.result

    def set_res(self, value):
        self.result = value


    def to_string(self):
        return f"{self.ope1} {self.operator} {self.ope2} = {self.result}"