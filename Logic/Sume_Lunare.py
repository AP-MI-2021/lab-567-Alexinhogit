from Domain.cheltuiala import get_luna, get_data, get_nr_ap, get_suma

def sume_lunare(lst_cheltuieli):
    """
    Functia va returna sumele lunare pe apartamente.
    :param lst_cheltuieli: Lista cu cheltuieli.
    :return: Dictionar de dictionare cu sumele lunare pe apartament.
    """
    sume = {}
    for cheltuiala in lst_cheltuieli:
        luna = get_luna(get_data(cheltuiala))
        ap = get_nr_ap(cheltuiala)

        if luna not in sume:
            sume[luna] = {}

        if ap in sume[luna]:
            sume[luna][ap] += get_suma(cheltuiala)
        else:
            sume[luna][ap] = get_suma(cheltuiala)

    return sume
