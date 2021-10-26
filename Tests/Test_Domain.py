from Domain.cheltuiala import creeaza_cheltuiala, get_id, get_nr_ap, get_suma, get_data, get_tip


def test_domain():
    cheltuiala = creeaza_cheltuiala(1, 3, 1000, '20.11.2021', 'canal')

    assert get_id(cheltuiala) == 1
    assert get_nr_ap(cheltuiala) == 3
    assert get_suma(cheltuiala) == 1000
    assert get_data(cheltuiala) == '20.11.2021'
    assert get_tip(cheltuiala) == 'canal'
