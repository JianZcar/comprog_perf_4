"""Computes the total of all the odd numbers from 1 up to the (n) as an inputted integer from the user."""


def main() -> tuple:
    """main function"""
    print("--- Total of Odd Numbers ---")
    input_number = input("> ")
    while True:
        try:
            input_number = int(input_number)
            if input_number < 0:
                raise ValueError
            odds = total_odd(input_number)
            (lambda: [print("Odd numbers:", str(odds[1]).replace("[", "").replace("]", "")),
                      print("Total:", odds[0])])()
            return odds[0], odds[1]
        except ValueError:
            print("Invalid input. Try again.")


def total_odd(n: int) -> tuple:
    """computes the total of all the odd numbers from 1 up to the (n) as an inputted integer from the user"""
    return sum(range(1, n+1, 2)), [i for i in range(1, n+1, 2)]
