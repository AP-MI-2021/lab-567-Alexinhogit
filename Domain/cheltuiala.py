def creeaza_cheltuiala(id, nr_ap, suma, data, tip):
    """
    Functia creeaza si returneaza un dictionar care reprezinta o cheltuiala.
    :param id: Id-ul cu ajutorul caruia identificam cheltuiala.
    :param nr_ap: Numarul apartamentului.
    :param suma: Suma cheltuielii.
    :param data: Data in care primeste cheltuiala.
    :param tip: Tipul cheltuielii(intretinere, canal sau alte cheltuieli)
    :return: Dictionarul returnat.
    """
    return {
        "id": id,
        "nr_ap": nr_ap,
        "suma": suma,
        "data": data,
        "tip": tip
    }


def get_id(cheltuiala):
    """
    Returneaza id-ul unei cheltuieli.
    :param cheltuiala: Cheltuiala a carei id va fi returnat.
    :return: Id-ul returnat.
    """
    return cheltuiala['id']

def get_nr_ap(cheltuiala):
    """
    Returneaza numarul apartamentului cheltuielii.
    :param cheltuiala: Cheltuiala a carei numar de apartament va fi returnat.
    :return: Numarul apartamentului returnat.
    """
    return cheltuiala['nr_ap']

def get_suma(cheltuiala):
    """
    Returneaza suma cheltuielii.
    :param cheltuiala: Cheltuiala a carei sume va fi returnata.
    :return: Suma returnata.
    """
    return cheltuiala['suma']

def get_data(cheltuiala):
    """
    Returneaza data cheltuielii.
    :param cheltuiala: Cheltuiala a carei data va fi returnata.
    :return: Data returnata.
    """
    return cheltuiala['data']

def get_luna(data):
    """
    Returneaza luna cheltuielii
    :param data: Data cheltuielii.
    :return: Luna cheltuielii.
    """
    return data[3:5]

def get_tip(cheltuiala):
    """
    Returneaza tipul cheltuielii.
    :param cheltuiala: Cheltuiala a carei tip va fi returnat.
    :return: Tipul returnat.
    """
    return cheltuiala['tip']

def set_suma(cheltuiala, suma):
    cheltuiala['suma'] = suma

def to_string(cheltuiala):
    """
    Returneaza dictionarul cu cheltuiala converit in string.
    :param cheltuiala: Cheltuiala ca dictionar.
    :return: Cheltuiala ca string.
    """
    return f"id:{get_id(cheltuiala)}, nr_ap:{get_nr_ap(cheltuiala)}, suma:{get_suma(cheltuiala)}, " \
           f"data:{get_data(cheltuiala)}, tip:{get_tip(cheltuiala)}"
