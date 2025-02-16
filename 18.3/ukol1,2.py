import time

# Globální proměnná, pokud potřebujete (např. pro úkol 1)
vysledek = []


def permutuj(uz_hotovo, zbyvajici_prvky, vysl_list):
    if not zbyvajici_prvky:
        vysl_list.append(uz_hotovo)
    else:
        for i in range(len(zbyvajici_prvky)):
            permutuj(
                uz_hotovo + [zbyvajici_prvky[i]],
                zbyvajici_prvky[:i] + zbyvajici_prvky[i + 1:],
                vysl_list
            )


def measure_permutations(n):
    pole = list(range(1, n + 1))
    temp_vysl = []
    start_time = time.time()
    permutuj([], pole, temp_vysl)
    end_time = time.time()
    return end_time - start_time, len(temp_vysl)


if __name__ == "__main__":
    print("=== ÚKOL 1: Měření času s výpisem permutací pro n=4 ===")
    start_time = time.time()
    pole = [7, 19, 23, 34]
    permutuj([], pole, vysledek)
    end_time = time.time()

    for perm in vysledek:
        print(perm)
    print(f"Počet permutací: {len(vysledek)}")
    print(f"Doba běhu: {end_time - start_time:.6f} s\n")

    print("=== ÚKOL 2: Měření času (bez výpisu) pro n = 4..12 ===")
    test_values = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    for n in test_values:
        doba, pocet = measure_permutations(n)
        print(f"n = {n}: čas = {doba:.6f} s, permutací = {pocet}")
