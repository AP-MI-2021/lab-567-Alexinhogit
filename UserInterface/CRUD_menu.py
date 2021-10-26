from Logic.CRUD import adaugare, stergere, modificare
from Domain.cheltuiala import creeaza_cheltuiala


def meniu_adaugare(lst_cheltuieli):
    id = int(input('Introduceti id-ul cheltuielii: '))
    nr_ap = int(input('Introduceti numarul apartamentului: '))
    suma = int(input('Introduceti suma cheltuielii: '))
    data = input('Introduceti data in care s-a emis cheltuiala in format DD.MM.YYYY: ')
    tip = input('Introduceti tipul cheltuielii: ')
    lst_cheltuieli = adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip)
    return lst_cheltuieli

def meniu_stergere(lst_cheltuieli):
    id = int(input('Introduceti id-ul cheltuielii care va fi stearsa: '))
    lst_cheltuieli = stergere(lst_cheltuieli, id)

    return lst_cheltuieli

def meniu_modificare(lst_cheltuieli):
    id = int(input('Introduceti id-ul cheltuielii care doriti sa se modifice: '))
    nr_ap = int(input('Introduceti un nou numar de apartament: '))
    suma = int(input('Introduceti o noua suma a cheltuielii: '))
    data = input('Introduceti noua data a cheltuielii: ')
    tip = input('Introduceti noul tip al cheltuielii: ')
    new_cheltuiala = creeaza_cheltuiala(id, nr_ap, suma, data, tip)
    return modificare(lst_cheltuieli, new_cheltuiala)