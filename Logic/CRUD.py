from Domain.cheltuiala import creeaza_cheltuiala, get_id

def adaugare(lst_cheltuieli, id, nr_ap, suma, data, tip):
    """
    Adauga o cheltuiala noua in lista de cheltuieli.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id: Id-ul cheltuielii.
    :param nr_ap: Nr. apartamentului cheltuielii.
    :param suma: Suma cheltuielii.
    :param data: Data cheltuielii.
    :param tip: Tipul cheltuielii.
    :return: Lista de cheltuieli.
    """
    lst_cheltuieli.append(creeaza_cheltuiala(id, nr_ap, suma, data, tip))
    return lst_cheltuieli

def stergere(lst_cheltuieli, id):
    """
    Sterge cheltuiala cu un anumit id din lista cu cheltuieli.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param id: Id-ul cheltuielii sterse.
    :return: Noua lista cu cheltuieli.
    """
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != id:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli

def modificare(lst_cheltuieli, new_cheltuiala):
    """
    Modifica una din cheltuielile din lista.
    :param lst_cheltuieli: Lista de cheltuieli.
    :param new_cheltuiala: Noua cheltuiala cu toti parametrii doriti modificati.
    :return: Lista cu cheltuieli.
    """
    new_lst_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_lst_cheltuieli.append(cheltuiala)
        else:
            new_lst_cheltuieli.append(new_cheltuiala)
    return new_lst_cheltuieli
