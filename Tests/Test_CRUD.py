from Logic.CRUD import adaugare, stergere, modificare
from Domain.cheltuiala import creeaza_cheltuiala, get_data, get_tip, get_id, get_nr_ap, get_suma

def test_adaugare():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    assert get_id(cheltuieli[0]) == 1
    assert get_nr_ap(cheltuieli[0]) == 3
    assert get_suma(cheltuieli[0]) == 1000
    assert get_data(cheltuieli[0]) == '20.11.2021'
    assert get_tip(cheltuieli[0]) == 'canal'

def test_stergere():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = stergere(cheltuieli, 1)
    assert len(cheltuieli) == 0

def test_modificare():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuiala_noua = creeaza_cheltuiala(1, 4, 2000, '24.11.2021', 'intretinere')
    new_lst_cheltuieli = modificare(cheltuieli, cheltuiala_noua)
    assert len(new_lst_cheltuieli) == len(cheltuieli)
    assert cheltuiala_noua not in cheltuieli
    assert cheltuiala_noua in new_lst_cheltuieli
