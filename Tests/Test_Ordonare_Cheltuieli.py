from Logic.CRUD import adaugare
from Logic.Ordonare_Cheltuieli import ordonare_cheltuieli_descrescator


def test_ordonare_cheltuieli_descrescator():
    cheltuieli = []

    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '23.12.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200.01, '21.12.2021', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 4, 9, 2000.03, '22.12.2021', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 4, 9, 2000.02, '22.12.2021', 'intretinere')

    cheltuiala1 = cheltuieli[0]
    cheltuiala2 = cheltuieli[1]
    cheltuiala3 = cheltuieli[2]
    cheltuiala4 = cheltuieli[3]

    assert ordonare_cheltuieli_descrescator(cheltuieli) == [cheltuiala3, cheltuiala4, cheltuiala2, cheltuiala1]
