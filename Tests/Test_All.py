from Tests.Test_Domain import test_domain
from Tests.Test_CRUD import test_adaugare, test_stergere, test_modificare

def all_tests():
    test_domain()
    test_adaugare()
    test_stergere()
    test_modificare()

