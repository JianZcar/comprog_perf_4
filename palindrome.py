"""Checks if a certain string or number from the user is palindrome or
not and display the last three characters or integer of the palindrome."""


def main() -> dict:
    """main function"""
    print("--- Palindrome ---")
    string_ = input("> ")
    a_palindrome = palindrome(string_)
    last_3 = last_three(string_)
    (lambda: [print("Is palindrome?", a_palindrome), print("Last three characters:", last_3)])()
    return {"Input: ": string_, "Is palindrome? ": a_palindrome, "Last three characters: ": last_3}


def palindrome(n: str) -> bool:
    """checks if a string or number is palindrome or not"""
    if n.lower() == n[::-1].lower():
        return True
    else:
        return False


def last_three(n: str) -> str:
    """returns the last three characters of a string or number"""
    return n[-3:]
