from Domain.cheltuiala import creeaza_cheltuiala, get_id, get_nr_ap, get_suma, get_data, get_tip, set_suma


def add_suma_for_cheltuieli_in_data(lst_cheltuieli, data, valoare):
    """
    Functia adauga o valoare la suma tuturor cheltuielilor dintr-o data anume.
    :param lst_cheltuieli: Lista de cheltuieli initiala.
    :param data: Data pentru care vor fi facute adaugarile la suma.
    :param valoare: Valoarea care va fi adunata la suma.
    :return: Lista de cheltuieli dupa adunarea valorii.
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        cheltuieli_new = creeaza_cheltuiala(get_id(cheltuiala), get_nr_ap(cheltuiala), get_suma(cheltuiala),
                                            get_data(cheltuiala), get_tip(cheltuiala))
        if data in get_data(cheltuiala):
            suma_marita = get_suma(cheltuiala) + valoare
            set_suma(cheltuieli_new, suma_marita)
        new_lst_cheltuieli.append(cheltuieli_new)
    return new_lst_cheltuieli
