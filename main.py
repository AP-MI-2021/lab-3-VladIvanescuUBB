def print_menu():
    print("4. Cea mai lunga subsecventa de numere ordonate crescător.")
    print("14. Cea mai lunga subsecventa de numere care au partea întreagă egală cu partea fracționară.")
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
        elif optiune == 0:
            break
        else:
            print("optiune invalida. Mai incearca!")


main()
