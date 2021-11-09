from Logic.CRUD import adaugare, stergere, modificare
from Logic.validari import validari_input, validare_id
from Domain.cheltuiala import to_string


def help_menu():
    print("""
    help                                    - arata acest meniu
    add,<id>,<nr_ap>,<suma>,<data>,<tip>    - adauga o cheltuiala
    remove,<id>                             - sterge o cheltuiala
    showall                                 - arata toate cheltuielile
    exit                                    - inchide programul
    """)

def add(cheltuieli, parameters):
    id = parameters[1]
    nr_ap = parameters[2]
    suma = parameters[3]
    data = parameters[4]
    tip = parameters[5]
    try:
        id, nr_ap, suma, data, tip = validari_input(id, nr_ap, suma, data, tip)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        cheltuieli = adaugare(cheltuieli, id, nr_ap, suma, data, tip)
        print("Cheltuiala adaugata.")

    return cheltuieli

def remove(cheltuieli, parameters):
    id = parameters[1]
    try:
        id = validare_id(id)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Cheltuiala stearsa.")
    return stergere(cheltuieli, id)

def edit(cheltuieli, parameters):
    id = parameters[1]
    nr_ap = parameters[2]
    suma = parameters[3]
    data = parameters[4]
    tip = parameters[5]
    try:
        id, nr_ap, suma, data, tip = validari_input(id, nr_ap, suma, data, tip)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        lst_cheltuieli = adaugare(cheltuieli, id, nr_ap, suma, data, tip)
        cheltuieli = modificare(lst_cheltuieli, cheltuieli)
        print("Cheltuiala modificata.")
    return cheltuieli

def showall(cheltuieli):
    for cheltuiala in cheltuieli:
        print(to_string(cheltuiala))

def run_command_line(cheltuieli):
    should_exit = False
    while not should_exit:
        print("Introduceti comanda: (comenzile se separa prin ; iar parametrii unei comenzi prin ,)")
        raw_cmd = input()

        cmds = raw_cmd.split(";")
        for cmd in cmds:
            parameters = cmd.split(",")

            if parameters[0] == "help":
                help_menu()
            elif parameters[0] == "add":
                cheltuieli = add(cheltuieli, parameters)
            elif parameters[0] == "remove":
                cheltuieli = remove(cheltuieli, parameters)
            elif parameters[0] == "edit":
                cheltuieli = edit(cheltuieli, parameters)
            elif parameters[0] == "showall":
                showall(cheltuieli)
            elif parameters[0] == "exit":
                should_exit = True
            else:
                print("Comanda invalida")
