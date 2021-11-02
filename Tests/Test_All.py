from Tests.Test_Domain import test_domain
from Tests.Test_CRUD import test_adaugare, test_stergere, test_modificare
from Tests.Test_Adunare_Valoare import test_add_suma_for_cheltuieli_in_data
from Tests.Test_Max_Tip_Cheltuieli import test_max_suma_for_tip_cheltuieli
from Tests.Test_Ordonare_Cheltuieli import test_ordonare_cheltuieli_descrescator
from Tests.Test_Sterge_Cheltuieli_Apartament import test_stergere_cheltuieli_apartament


def all_tests():
    test_domain()
    test_adaugare()
    test_stergere()
    test_modificare()
    test_add_suma_for_cheltuieli_in_data()
    test_max_suma_for_tip_cheltuieli()
    test_ordonare_cheltuieli_descrescator()
    test_stergere_cheltuieli_apartament()
