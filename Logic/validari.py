import re

def validari_input(id, nr_ap, suma, data, tip):
    errors = []
    try:
        id = int(id)
        if id < 0:
            errors.append('ID-ul nu poate fi numar negativ.')
    except ValueError:
        errors.append('ID-ul trebuie sa fie numar intreg.')

    try:
        nr_ap = int(nr_ap)
        if nr_ap < 0:
            errors.append('Numarul apartamentului trebuie sa fie pozitiv')
    except ValueError:
        errors.append('Numarul apartamentului trebuie sa fie numar intreg')

    try:
        suma = float(suma)
        if suma < 0:
            errors.append('Suma trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append('Suma trebuie sa fie un numar real')

    # Regex pattern care verifica daca data este intr-un format corect (DD/MM/YYYY; DD-MM-YYYY; DD.MM.YYYY)
    # si daca data exista (Sa nu se depaseasca numarul de zile din luna respectiva, sa nu se depaseasca 12 luni
    # si sa se tina cont de anii bisecti)
    date_check_pattern = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])"
                                    r"\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?"
                                    r":0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-"
                                    r"9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
    if date_check_pattern.match(data) is None:
        errors.append("Data introdusa nu exista, va rog introduceti o data valida.")

    if tip != "canal" and tip != "intretinere" and tip != "alte cheltuieli":
        errors.append("Tipul trebuie sa fie unul din cele precizate (canal / intretinere / alte cheltuieli)")

    if len(errors) != 0:
        raise ValueError(errors)

    return id, nr_ap, suma, data, tip

def validare_id(id):
    errors = []
    try:
        id = int(id)
        if id < 0:
            errors.append('ID-ul nu poate fi numar negativ.')
    except ValueError:
        errors.append('ID-ul trebuie sa fie numar intreg.')

    if len(errors) != 0:
        raise ValueError(errors)

    return id

def validare_nr_ap(nr_ap):
    errors = []
    try:
        nr_ap = int(nr_ap)
        if nr_ap < 0:
            errors.append('Numarul apartamentului trebuie sa fie pozitiv')
    except ValueError:
        errors.append('Numarul apartamentului trebuie sa fie numar intreg')

    if len(errors) != 0:
        raise ValueError(errors)

    return nr_ap


def validare_add_suma_for_cheltuieli_in_data(valoare, data):
    errors = []
    try:
        valoare = float(valoare)
        if valoare < 0:
            errors.append('Valoarea trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append('Valoarea trebuie sa fie un numar real')

    # Regex pattern care verifica daca data este intr-un format corect (DD/MM/YYYY; DD-MM-YYYY; DD.MM.YYYY)
    # si daca data exista (Sa nu se depaseasca numarul de zile din luna respectiva, sa nu se depaseasca 12 luni
    # si sa se tina cont de anii bisecti)
    date_check_pattern = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])"
                                    r"\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?"
                                    r":0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-"
                                    r"9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")
    if date_check_pattern.match(data) is None:
        errors.append("Data introdusa nu exista, va rog introduceti o data valida.")

    if len(errors) != 0:
        raise ValueError(errors)

    return valoare, data
