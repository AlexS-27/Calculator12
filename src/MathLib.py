class MathLib:

    def __init__(self, math_request, result):
        self.math_request = math_request
        self.res = result

    @classmethod
    def execute(cls, math_request):
        ope1 = math_request.get_ope1()
        operator = math_request.get_operator()
        ope2 = math_request.get_ope2()

        match operator:
            case 'add':
                math_request.get_res(ope1 + ope2)
            case 'sub':
                math_request.get_res(ope1 - ope2)
            case 'mul':
                math_request.get_res(ope1 * ope2)
            case 'div':
                if ope2 == 0:
                    raise MathLibException()
                math_request.get_res(ope1 / ope2)
            case 'pow':
                math_request.get_res(ope1 ** ope2)
            case 'root':
                math_request.get_res(cls.__root(ope1,ope2))
            case _:
                OperatorNotSupportedException.get_valid_operator(math_request)

    @staticmethod
    def __root(ope1, ope2):
        if ope2 == 0:
            raise ValueError("Impossible to calculate the root of 0")
        elif ope1 < 0 and ope2 %2 == 0:
            raise ValueError("Impossible to calculate the root of a negative number")
        else:
            return round(ope1**(1/ope2),2)

class MathLibException(Exception):
    def __init__(self, message="division by zero is undefined"):
        self.message = message
        super().__init__(self.message)

class OperatorNotSupportedException(MathLibException):
    @staticmethod
    def get_valid_operator(math_request):
        valid_operator = ['add', 'sub', 'mul', 'div', 'pow', 'root']

        if math_request.operator not in valid_operator:
            raise OperatorNotSupportedException(f"Operator '{math_request.operator} is not supported")