from Domain.cheltuiala import get_suma
from Logic.CRUD import adaugare
from Logic.Adunare_Valoare import add_suma_for_cheltuieli_in_data


def test_add_suma_for_cheltuieli_in_data():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 2, 7, 2400, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'intretinere')

    cheltuieli = add_suma_for_cheltuieli_in_data(cheltuieli, '20.11.2021', 56)
    assert get_suma(cheltuieli[0]) == 1056
    assert get_suma(cheltuieli[1]) == 2456

    cheltuieli = add_suma_for_cheltuieli_in_data(cheltuieli, '24.11.2021', 5434)

    cheltuieli = add_suma_for_cheltuieli_in_data(cheltuieli, '20.11.2021', 14)
    assert get_suma(cheltuieli[0]) == 1070
    assert get_suma(cheltuieli[1]) == 2470

    cheltuieli = add_suma_for_cheltuieli_in_data(cheltuieli, '21.12.2021', 13.5)
    assert get_suma(cheltuieli[2]) == 213.5
