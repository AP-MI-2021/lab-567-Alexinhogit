from UserInterface.CRUD_menu import meniu_adaugare, meniu_stergere, meniu_modificare
from Domain.cheltuiala import to_string
from Logic.Sterge_Cheltuieli_Apartament import stergere_cheltuieli_apartament
from Logic.Adunare_Valoare import add_suma_for_cheltuieli_in_data
from Logic.Max_Tip_Cheltuieli import max_suma_for_tip_cheltuiala
from Logic.Ordonare_Cheltuieli import ordonare_cheltuieli_descrescator
from Logic.Sume_Lunare import sume_lunare
from Logic.validari import validare_nr_ap, validare_add_suma_for_cheltuieli_in_data
import copy


def afisare_cheltuieli(lst_cheltuieli):
    for cheltuiala in lst_cheltuieli:
        print(to_string(cheltuiala))

def meniu_stergere_cheltuieli_apartament(lst_cheltuieli):
    nr_ap = input('Introduceti numarul apartamentului pentru care doriti sa stergeti toate cheltuielile:')
    try:
        nr_ap = validare_nr_ap(nr_ap)
        lst_cheltuieli = stergere_cheltuieli_apartament(lst_cheltuieli, nr_ap)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Cheltuieli sterse.")
    return lst_cheltuieli

def meniu_add_suma_for_cheltuieli_in_data(lst_cheltuieli):
    valoare = input("Ce valoare doriti sa adunati?:")
    data = input("Cheltuielilor din data:")
    try:
        valoare, data = validare_add_suma_for_cheltuieli_in_data(valoare, data)
        lst_cheltuieli = add_suma_for_cheltuieli_in_data(lst_cheltuieli, data, valoare)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Valoarea a fost adaugata cheltuielilor aferente.")
    return lst_cheltuieli

def meniu_max_suma_for_tip_cheltuiala(lst_cheltuieli):
    intretinere, canal, alte_cheltuieli = max_suma_for_tip_cheltuiala(lst_cheltuieli)
    print(f"intretinere: {intretinere}")
    print(f"canal: {canal}")
    print(f"alte cheltuieli: {alte_cheltuieli}")

def meniu_sume_lunare(lst_cheltuieli):
    sume = sume_lunare(lst_cheltuieli)
    for luna in sume:
        print("Luna " + luna + ":")
        for apartament in sume[luna]:
            print("Apartamentul " + str(apartament) + ": " + str(sume[luna][apartament]))

def run_menu(lst_cheltuieli):
    istoric = [[]]
    index = 0

    while True:
        print("""
        1. Adaugare cheltuiala.
        2. Stergere cheltuiala.
        3. Modificare cheltuiala.
        4. Stergerea tuturor cheltuielilor pentru un apartament dat.
        5. Adunarea unei valori la toate cheltuielile dintr-o data citita.
        6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuiala.
        7. Ordonarea cheltuielilor descrescator după suma.
        8. Afisarea sumelor lunare pentru apartament.
        a. Afisarea tuturor cheltuielilor.
        u. Undo.
        r. Redo.
        x. Iesire """)

        cmd = input("Comanda: ")
        if cmd == '1':
            lst_cheltuieli = meniu_adaugare(lst_cheltuieli)
        elif cmd == '2':
            lst_cheltuieli = meniu_stergere(lst_cheltuieli)
        elif cmd == '3':
            lst_cheltuieli = meniu_modificare(lst_cheltuieli)
        elif cmd == '4':
            lst_cheltuieli = meniu_stergere_cheltuieli_apartament(lst_cheltuieli)
        elif cmd == '5':
            lst_cheltuieli = meniu_add_suma_for_cheltuieli_in_data(lst_cheltuieli)
        elif cmd == '6':
            meniu_max_suma_for_tip_cheltuiala(lst_cheltuieli)
        elif cmd == '7':
            print(ordonare_cheltuieli_descrescator(lst_cheltuieli))
        elif cmd == '8':
            meniu_sume_lunare(lst_cheltuieli)

        elif cmd == 'u':
            if index > 0:
                index -= 1
            lst_cheltuieli = istoric[index]
        elif cmd == 'r':
            if index < len(istoric) - 1:
                index += 1
            lst_cheltuieli = istoric[index]

        elif cmd == 'a':
            afisare_cheltuieli(lst_cheltuieli)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida.")

        if cmd in ['1', '2', '3', '4', '5']:
            istoric = istoric[:index+1]
            istoric.append(copy.deepcopy(lst_cheltuieli))
            index = len(istoric) - 1
            lst_cheltuieli = istoric[-1]
