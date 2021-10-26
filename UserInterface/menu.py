from UserInterface.CRUD_menu import meniu_adaugare, meniu_stergere, meniu_modificare
from Domain.cheltuiala import to_string


def afisare_cheltuieli(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(to_string(cheltuiala))

def run_menu(lst_cheltuieli):
    while True:
        print("""
        1. Adaugare cheltuiala.
        2. Stergere cheltuiala.
        3. Modificare cheltuiala. 
        a. Afisarea tuturor cheltuielilor.
        x. Iesire """)

        cmd = input("Comanda: ")
        if cmd == '1':
            lst_cheltuieli = meniu_adaugare(lst_cheltuieli)
        elif cmd == '2':
            lst_cheltuieli = meniu_stergere(lst_cheltuieli)
        elif cmd == '3':
            lst_cheltuieli = meniu_modificare(lst_cheltuieli)
        elif cmd == 'a':
            afisare_cheltuieli(lst_cheltuieli)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida.")
