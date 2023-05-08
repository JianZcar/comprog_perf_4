import odd_number as odd
import palindrome as pal
import ui
import file_handler as fh


def main() -> None:
    """main function"""
    menu_items = {"Calculate the Total of Odd Numbers": odd.main,
                  "Check if Palindrome": pal.main,
                  "Exit": exit}
    t_value = ui.menu(menu_items)
    fh.main(t_value, "FileHandling.txt")
    print("\n")
    main()


if __name__ == "__main__":
    main()
