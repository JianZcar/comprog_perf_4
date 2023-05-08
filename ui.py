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


def main(items: dict, **kwargs) -> dict:
    """displays the menu"""
    [print(f"{index + 1}. {item}") for index, item in enumerate(items.keys())]
    input_option = input_number(len(items))
    return items[list(items.keys())[input_option - 1]]()
