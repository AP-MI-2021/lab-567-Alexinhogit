from Domain.cheltuiala import get_suma


def ordonare_cheltuieli_descrescator(lst_cheltuieli):
    """
    Functia ordoneaza cheltuielile din lista in ordine descrescatoare pentru suma.
    :param lst_cheltuieli: Lista cu cheltuielile.
    :return: Lista cu cheltuielile ordonata descrescator dupa suma.
    """
    for i in range(0, len(lst_cheltuieli)):
        for j in range(i + 1, len(lst_cheltuieli)):
            if get_suma(lst_cheltuieli[i]) < get_suma(lst_cheltuieli[j]):
                lst_cheltuieli[i], lst_cheltuieli[j] = lst_cheltuieli[j], lst_cheltuieli[i]

    return lst_cheltuieli
