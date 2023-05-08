"""UI of the program"""


def input_number(max_n: int) -> int:
    """asks the user to input a number"""
    while True:
        try:
            number = int(input("> "))
            if number < 0 or number > max_n:
                raise ValueError
            return number
        except ValueError:
            print("Invalid input. Try again.")


def menu(items: dict) -> tuple:
    """displays the menu"""
    [print(f"{index + 1}. {item}") for index, item in enumerate(items.keys())]
    input_option = input_number(len(items))
    item = items[list(items.keys())[input_option - 1]]()
    return item
