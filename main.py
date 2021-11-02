from Tests.Test_All import all_tests
from UserInterface.menu import run_menu


def main():
    all_tests()
    lst_cheltuieli = []
    run_menu(lst_cheltuieli)


if __name__ == "__main__":
    main()
