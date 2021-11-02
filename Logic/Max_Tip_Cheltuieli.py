from Domain.cheltuiala import get_suma, get_tip


def max_suma_for_tip_cheltuiala(lst_cheltuieli):
    """
    Functia determina cea mai mare suma pentru fiecare tip de cheltuiala.
    :param lst_cheltuieli: Lista verificata.
    :return: Lista cu cea mai mare suma pentru fiecare tip de cheltuiala.
    """
    max_canal = 0
    max_intretinere = 0
    max_alte_cheltuieli = 0

    for cheltuiala in lst_cheltuieli:
        if get_tip(cheltuiala) == "intretinere":
            if float(get_suma(cheltuiala)) > max_intretinere:
                max_intretinere = float(get_suma(cheltuiala))
        elif get_tip(cheltuiala) == "canal":
            if float(get_suma(cheltuiala)) > max_canal:
                max_canal = float(get_suma(cheltuiala))
        elif get_tip(cheltuiala) == "alte cheltuieli":
            if float(get_suma(cheltuiala)) > max_alte_cheltuieli:
                max_alte_cheltuieli = float(get_suma(cheltuiala))

    return [max_intretinere, max_canal, max_alte_cheltuieli]
