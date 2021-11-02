from Logic.CRUD import adaugare
from Logic.Max_Tip_Cheltuieli import max_suma_for_tip_cheltuiala


def test_max_suma_for_tip_cheltuieli():
    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 2, 7, 2400, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'intretinere')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'alte cheltuieli')

    assert max_suma_for_tip_cheltuiala(cheltuieli) == [200.0, 2400.0, 200.0]

    cheltuieli = []
    cheltuieli = adaugare(cheltuieli, 1, 3, 1000, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 2, 7, 2400, '20.11.2021', 'canal')
    cheltuieli = adaugare(cheltuieli, 4, 9, 200, '21.12.2021', 'intretinere')

    assert max_suma_for_tip_cheltuiala(cheltuieli) == [200.0, 2400.0, 0.0]
