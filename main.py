def print_menu():
    print("4. Cea mai lunga subsecventa de numere ordonate crescător.")
    print("14. Cea mai lunga subsecventa de numere care au partea întreagă egală cu partea fracționară.")
    print("2. Cea mai lunga secventa de numere prime.")
    print("0. Iesire")


def citire_lista():
    """
    functia citeste o lista
    :return: lista citita
    """
    l = []
    n = int(input("dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def crescator(lista):
    """
    functia verifica daca toate elementele dintr-o lista sunt ordonate crescator
    :param lista: o lista de numere intregi
    :return: True, daca lista este ordonata crescator sau False in caz contrar
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def test_crescator():
    """
    teste pentru functia crescator
    """
    assert crescator([]) is True
    assert crescator([1, 2, 3]) is True
    assert crescator([3, 2, 1]) is False
    assert crescator([1, 3, 2]) is False
    assert crescator([1, -2, 5]) is False


def get_longest_sorted_asc(lista) -> list[int]:
    """
    functia determina cea mai lunga subsecventa de numere ordonate crescător
    :param lista: lista de numere intregi
    :return: cea mai lunga subsecventa de numere ordonate crescător din lista
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if crescator(lista[i:j + 1]) and len(lista[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = lista[i:j + 1]
    return subsecventa_max


def test_get_longest_sorted_asc():
    """
    teste pentru functia get_longest_sorted_asc
    """
    assert get_longest_sorted_asc([]) == []
    assert get_longest_sorted_asc([1, 2, 3]) == [1, 2, 3]
    assert get_longest_sorted_asc([3, 2, 1]) == [3]
    assert get_longest_sorted_asc([1, 2, 1, 2, 3, 1]) == [1, 2, 3]
    assert get_longest_sorted_asc([1, 2, 3, 1, 2]) == [1, 2, 3]


def p_intreaga_egala_cu_p_fractionara(lista):
    """
    functia verifica daca toate elementele din lista au partea intreaga egala cu partea fractionara
    :param lista: lista de numere intregi
    :return: True, daca toate numerele din lista au partea intreaga egala cu partea fractionara sau False in caz contrar
    """
    for i in range(len(lista)):
        if lista[i] != 0:
            return False
    return True


def test_p_intreaga_egala_cu_p_fractionara():
    """
    teste pentru functia p_intreaga_egala_cu_p_fractionara
    """
    assert p_intreaga_egala_cu_p_fractionara([]) is True
    assert p_intreaga_egala_cu_p_fractionara([1, 2, 3]) is False
    assert p_intreaga_egala_cu_p_fractionara([0]) is True
    assert p_intreaga_egala_cu_p_fractionara([1, -2, 0]) is False
    assert p_intreaga_egala_cu_p_fractionara([0, 0, 0, 0]) is True


def get_longest_equal_int_real(lista) -> list[float]:
    """
    functia determina cea mai lunga subsecventa de numare care au partea întreagă egală cu partea fracționară
    :param lista: lista de numere intregi
    :return: cea mai lunga subsecventa de numare care au partea întreagă egală cu partea fracționară din lista
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if p_intreaga_egala_cu_p_fractionara(lista[i: j + 1]) and len(lista[i: j + 1]) > len(subsecventa_max):
                subsecventa_max = lista[i: j + 1]
    return subsecventa_max


def test_get_longest_equal_int_real():
    """
    teste pentru functia get_longest_equal_int_real
    """
    assert get_longest_equal_int_real([]) == []
    assert get_longest_equal_int_real([1, 2, 3]) == []
    assert get_longest_equal_int_real([1, 0, 2]) == [0]
    assert get_longest_equal_int_real([0, 0, 3]) == [0, 0]
    assert get_longest_equal_int_real([0, 0, 1, 0, 0, 0]) == [0, 0, 0]


def is_prime(x):
    """
    functia verifica daca un numar este prim sau nu
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def test_is_prime():
    """
    teste pentru functia is_prime
    """
    assert is_prime(-5) is False
    assert is_prime(2) is True
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(25) is False


def all_prime(lista):
    """
    functia verifica daca toate elementele din lista sunt prime
    :param lista: o lista de numere intregi
    :return: True, daca lista e formata doar din numere prime sau False in caz contrar
    """
    for i in range(0, len(lista)):
        if is_prime(lista[i]) is False:
            return False
    return True


def test_all_prime():
    """
    teste pentru functia all_prime()
    """
    assert all_prime([]) is True
    assert all_prime([3, 5, 7]) is True
    assert all_prime([10, 11, 13]) is False
    assert all_prime([10, 12, 25]) is False
    assert all_prime([7, 29, 13]) is True


def get_longest_all_primes(lista) -> list[int]:
    """
    functia calculeaza cea mai lunga secventa de numere prime dintr-o lista
    :param lista:o lista de numere intregi
    :return:cea mai lunga secventa de numere prime din lista
    """
    subsecventa_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if all_prime(lista[i: j + 1]) and len(lista[i: j + 1]) > len(subsecventa_max):
                subsecventa_max = lista[i: j + 1]
    return subsecventa_max


def test_get_longest_all_primes():
    """
    teste pentru functia get_longest_all_primes()
    """
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([1, 2, 3, 4, 5]) == [2, 3]
    assert get_longest_all_primes([4, 17, 13, 3, 10, 7, 11]) == [17, 13, 3]
    assert get_longest_all_primes([4, 6, 8]) == []
    assert get_longest_all_primes([3, 5, 7]) == [3, 5, 7]


def main():
    print_menu()
    while True:
        optiune = int(input("Alegeti optiunea: "))
        if optiune == 4:
            test_crescator()
            test_get_longest_sorted_asc()
            lista = citire_lista()
            print(get_longest_sorted_asc(lista))
        elif optiune == 14:
            test_p_intreaga_egala_cu_p_fractionara()
            test_get_longest_equal_int_real()
            lista = citire_lista()
            print(get_longest_equal_int_real(lista))
        elif optiune == 2:
            test_is_prime()
            test_all_prime()
            test_get_longest_all_primes()
            lista = citire_lista()
            print(get_longest_all_primes(lista))
        elif optiune == 0:
            break
        else:
            print("optiune invalida. Mai incearca!")


main()
