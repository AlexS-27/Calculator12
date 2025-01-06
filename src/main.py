from src.MathRequest import MathRequest
from src.MathLib import MathLib, OperatorNotSupportedException

def main():
    math_request = ask_user_input()
    math_request.get_res(MathLib.execute(math_request))
    display_result(math_request)

def ask_user_input() -> MathRequest:
    # Get first operand from the user
    ope1 = ask_user_float_input("Enter the first operand: ")

    # Get the operator from the user
    oper = input("Enter an operator (add, sub, mul, div, pow, root): ")

    # Get second operand from the user
    ope2 = ask_user_float_input("Enter the second operand: ")

    return MathRequest(ope1, oper, ope2)

def ask_user_float_input(msg):
    return float(input(msg))

def display_result(math_request):
    # Print the result
        print(math_request.to_string())


# Call the main function to run the program
main()