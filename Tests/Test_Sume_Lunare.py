from Logic.CRUD import adaugare
from Logic.Sume_Lunare import sume_lunare

def test_sume_lunare():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 2, 7, 2400, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 5, 9, 1200, '21.12.2021', 'alte cheltuieli')

    sume = sume_lunare(cheltuieli)
    assert len(sume) == 2
    assert len(sume["11"]) == 2
    assert sume["11"][3] == 1000
    assert sume["12"][9] == 1400
