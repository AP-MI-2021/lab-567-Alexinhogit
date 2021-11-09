from Tests.Test_All import all_tests
from UserInterface.menu import run_menu
from UserInterface.command_line_console import run_command_line

def main():
    all_tests()
    lst_cheltuieli = []
    interfata = input(f"Ce interfata doriti sa utilizati?\nCommand line (c) sau Meniu (m)?")

    if interfata == 'm':
        run_menu(lst_cheltuieli)
    elif interfata == 'c':
        run_command_line(lst_cheltuieli)


if __name__ == "__main__":
    main()
