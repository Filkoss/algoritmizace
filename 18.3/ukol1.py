import time

vysledek = []

def permutuj(uz_hotovo, zbyvajici_prvky):
    if not zbyvajici_prvky:
        vysledek.append(uz_hotovo)
    else:
        for i in range(len(zbyvajici_prvky)):
            permutuj(
                uz_hotovo + [zbyvajici_prvky[i]],
                zbyvajici_prvky[:i] + zbyvajici_prvky[i+1:]
            )

if __name__ == "__main__":
    # Měření času začíná
    start_time = time.time()

    # Původní pole
    pole = [7, 19, 23, 34]
    permutuj([], pole)

    # Výpis permutací
    for permutace in vysledek:
        print(permutace)

    # Měření času končí
    end_time = time.time()

    print(f"\nPočet permutací: {len(vysledek)}")
    print(f"Doba běhu: {end_time - start_time:.6f} s")
