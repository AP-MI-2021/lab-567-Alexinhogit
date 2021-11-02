from Logic.CRUD import adaugare, stergere, modificare
from Domain.cheltuiala import creeaza_cheltuiala
from Logic.validari import validari_input, validare_id


def meniu_adaugare(lst_cheltuieli):
    id = input('Introduceti id-ul cheltuielii: ')
    nr_ap = input('Introduceti numarul apartamentului: ')
    suma = input('Introduceti suma cheltuielii: ')
    data = input('Introduceti data in care s-a emis cheltuiala in format DD.MM.YYYY: ')
    tip = input('Introduceti tipul cheltuielii (intretinere / canal / alte cheltuieli): ')
    try:
        id, nr_ap, suma, data, tip = validari_input(id, nr_ap, suma, data, tip)
        lst_cheltuieli = adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Cheltuiala adaugata.")
    return lst_cheltuieli

def meniu_stergere(lst_cheltuieli):
    id = input('Introduceti id-ul cheltuielii care va fi stearsa: ')
    try:
        id = validare_id(id)
        lst_cheltuieli = stergere(lst_cheltuieli, id)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Cheltuiala stearsa.")
    return lst_cheltuieli

def meniu_modificare(lst_cheltuieli):
    id = input('Introduceti id-ul cheltuielii care doriti sa se modifice: ')
    nr_ap = input('Introduceti un nou numar de apartament: ')
    suma = input('Introduceti o noua suma a cheltuielii: ')
    data = input('Introduceti noua data a cheltuielii: ')
    tip = input('Introduceti noul tip al cheltuielii (intretinere / canal / alte cheltuieli): ')
    try:
        id, nr_ap, suma, data, tip = validari_input(id, nr_ap, suma, data, tip)
        new_cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
        lst_cheltuieli = modificare(lst_cheltuieli, new_cheltuiala)
    except ValueError as ve:
        print("Eroare:", ve)
    else:
        print("Cheltuiala modificata.")
    return lst_cheltuieli
