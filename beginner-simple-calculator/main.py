from art import logo

print(logo)


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    return number1 / number2


def validate_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Error: Please enter a number.")
        return validate_input(prompt)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(operation, number1, number2):
    if operation in operations:
        # send this like arguments
        return operations[operation](number1, number2)
    else:
        print("Error: Invalid operation symbol.")
        return None


def print_operations():
    for symbol in operations:
        print(symbol)


def get_operation():
    return input("Pick an operation from the line above: ")


def continue_with_answer(answer):
    first_number = answer
    second_number = validate_input("What's the next number?: ")
    return first_number, second_number


def new_calculation():
    first_number = validate_input("What's the first number?: ")
    second_number = validate_input("What's the second number?: ")
    return first_number, second_number


first_number, second_number = new_calculation()

while True:
    print_operations()
    operation = get_operation()
    answer = calculate(operation, first_number, second_number)

    if answer is not None:
        print(f"{first_number} {operation} {second_number} = {answer}")
    else:
        continue

    is_continue = input(
        f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'exit' to finish: ").lower()

    if is_continue == "n":
        first_number, second_number = new_calculation()
    elif is_continue == "y":
        first_number, second_number = continue_with_answer(answer)
    else:
        print("Goodbye!")
        break
