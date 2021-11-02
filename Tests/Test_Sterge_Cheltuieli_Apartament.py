from Logic.CRUD import adaugare
from Logic.Sterge_Cheltuieli_Apartament import stergere_cheltuieli_apartament


def test_stergere_cheltuieli_apartament():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 2, 7, 2400, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 5, 9, 1200, '21.12.2021', 'alte cheltuieli')

    cheltuieli = stergere_cheltuieli_apartament(cheltuieli, 2)

    assert len(cheltuieli) == 4

    cheltuieli = stergere_cheltuieli_apartament(cheltuieli, 7)

    assert len(cheltuieli) == 3

    cheltuieli = stergere_cheltuieli_apartament(cheltuieli, 9)

    assert len(cheltuieli) == 1

    cheltuieli = stergere_cheltuieli_apartament(cheltuieli, 3)
    
    assert len(cheltuieli) == 0
