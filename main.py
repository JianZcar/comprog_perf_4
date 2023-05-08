import odd_number as odd
import palindrome as pal
import ui
import file_handler as fh


def exit_program(temp: str) -> None:
    """exits the program"""
    temp_file = fh.FileHandler(temp)
    temp_file.write([])
    exit()


def main() -> None:
    """main function"""
    file_name = "file_handler"
    temp_file_name = "temp_file_handler"
    menu_items = {"Calculate the Total of Odd Numbers": odd.main,
                  "Check if Palindrome": pal.main,
                  "Save Data": lambda: fh.temp_file_handler(temp_file_name, file_name),
                  "Read Saves": lambda: fh.read(file_name),
                  "Delete Save": lambda: fh.delete_save(file_name),
                  "Exit": lambda: exit_program(temp_file_name)}

    temp_ = ui.main(menu_items)
    if temp_ is not None:
        fh.main(temp_, temp_file_name)
    print("\n")
    main()


if __name__ == "__main__":
    main()
