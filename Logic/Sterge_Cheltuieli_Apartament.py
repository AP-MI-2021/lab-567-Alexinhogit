from Domain.cheltuiala import get_nr_ap


def stergere_cheltuieli_apartament(lst_cheltuieli, nr_ap):
    """
    Functia sterge toate cheltuielile gasite aferente aceluias apartament.
    :param lst_cheltuieli: Lista de cheltuieli initiala.
    :param nr_ap: Apartamentul pentru care vor fi sterse toate cheltuielile.
    :return:
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if nr_ap != get_nr_ap(cheltuiala):
            new_lst_cheltuieli.append(cheltuiala)
    return new_lst_cheltuieli
