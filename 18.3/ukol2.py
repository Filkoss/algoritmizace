import time

def permutuj(uz_hotovo, zbyvajici_prvky, vysledek):
    """
    Rekurzivní funkce pro vygenerování všech permutací.
    Uz hotovo = část výsledné permutace,
    zbyvajici_prvky = prvky, které ještě nebyly přidány,
    vysledek = list, do kterého se ukládají hotové permutace.
    """
    if not zbyvajici_prvky:
        vysledek.append(uz_hotovo)
    else:
        for i in range(len(zbyvajici_prvky)):
            permutuj(
                uz_hotovo + [zbyvajici_prvky[i]],
                zbyvajici_prvky[:i] + zbyvajici_prvky[i+1:],
                vysledek
            )

def measure_permutations(n):
    """
    Vygeneruje všechny permutace pro seznam [1, 2, ..., n],
    změří dobu, kterou to zabere, a vrátí (doba_běhu, počet_permutací).
    """
    pole = list(range(1, n+1))
    vysledek = []

    start = time.time()
    permutuj([], pole, vysledek)
    end = time.time()

    doba_behu = end - start
    pocet_permutaci = len(vysledek)  # mělo by být n!
    return doba_behu, pocet_permutaci

if __name__ == "__main__":
    # Budeme měřit pro velikosti 4 až 12
    testovaci_velikosti = [4, 5, 6, 7, 8, 9, 10, 11, 12]

    print("n |   Doba běhu [s]   | Počet permutací")
    print("---------------------------------------")
    for n in testovaci_velikosti:
        doba, pocet = measure_permutations(n)
        print(f"{n} | {doba:.6f} s        | {pocet}")

    # Následně můžete hodnoty n a Doba_behu vykreslit
    # v libovolném tabulkovém procesoru či nástroji
    # (Excel, matplotlib, atd.) pro vizualizaci složitosti.
