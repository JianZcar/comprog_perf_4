"""stores data in a txt file"""
import pickle


class FileHandler:
    """stores data in a txt file"""
    def __init__(self, file_name):
        self.file_name = file_name + ".pickle"

    def write(self, data):
        """writes data to the file"""
        with open(self.file_name, "wb") as file:
            pickle.dump(data, file)

    def read(self):
        """reads data from the file"""
        with open(self.file_name, "rb") as file:
            return pickle.load(file)

    def delete_save(self):
        pass


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


def main(data: dict, file_name: str) -> None:
    """main function"""
    write(file_name, data)


def read(file_name: str) -> None:
    """reads data from the file"""
    try:
        print("\n")
        file = FileHandler(file_name)
        print("--- Saved Data ---")
        if len(file.read()) == 0:
            raise FileNotFoundError
        for index, i in enumerate(file.read()):
            print(f"-Save {index + 1}-")
            [print(f"{key}{value}") for key, value in i.items()]
            print("\n")
    except FileNotFoundError:
        print("No saved data found!")


def write(file_name: str, data_: dict) -> None:
    """writes data to the file"""
    try:
        file = FileHandler(file_name)
        save = file.read()
        save.append(data_)
        file.write(save)
    except FileNotFoundError:
        file = FileHandler(file_name)
        file.write([data_])


def temp_file_handler(temp_file_name: str, file_name: str) -> None:
    """creates a temporary file"""
    temp_data = FileHandler(temp_file_name)
    data = temp_data.read()
    if data is not None and data != []:
        for i in data:
            main(i, file_name)
        else:
            temp_data.write([])
            print("Data saved")
    else:
        print("No data to save")


def delete_save(file_name: str) -> None:
    """deletes a save"""
    try:
        save_number = input_number(len(FileHandler(file_name).read()))
        file = FileHandler(file_name)
        save = file.read()
        if len(save) == 0:
            raise FileNotFoundError
        del save[save_number - 1]
        file.write(save)
    except FileNotFoundError:
        print("No saved data found!")
