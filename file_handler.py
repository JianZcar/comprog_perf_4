"""stores data in a txt file"""


class FileHandler:
    """stores data in a txt file"""
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, data):
        """writes data to the file"""
        with open(self.file_name, "w") as file:
            file.write(data)

    def read(self):
        """reads data from the file"""
        with open(self.file_name, "r") as file:
            data = file.read()
        return data


def is_to_save() -> bool:
    """asks if the user wants to save the data"""
    while True:
        answer = input("Do you want to save the data? (y/n): ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Invalid input!")


def main(data: tuple, file_name: str) -> None:
    """main function"""
    is_save = is_to_save()
    if is_save:
        file = FileHandler(file_name)
        file.write(str(data))
        print("Data saved!")
    else:
        print("Data not saved!")
