import itertools
import random

def boat_brute_force(a, b, c):
    """
    Brute-force algoritmus:
    1) Vygenerujeme všech 6 možných permutací (tj. uspořádání) tří pasažérů.
    2) U každé permutace spočítáme 'rating' = (váha na pravoboku) - (váha na levoboku).
    3) Sledujeme, které permutace mají nejmenší absolutní hodnotu ratingu.
    4) Vrátíme všechny takto nejlepší permutace + příslušnou minimální hodnotu |rating|.

    Tato funkce je deterministická: vždy vrací stejné výsledky pro stejné vstupy.
    """
    passengers = [a, b, c]
    best_solutions = []
    best_abs_diff = None

    for perm in itertools.permutations(passengers):
        left, center, right = perm
        rating = right - left  # kladné => těžší vpravo, záporné => těžší vlevo

        # Minimalizujeme absolutní hodnotu rozdílu
        if best_abs_diff is None or abs(rating) < best_abs_diff:
            best_abs_diff = abs(rating)
            best_solutions = [perm]
        elif abs(rating) == best_abs_diff:
            best_solutions.append(perm)

    return best_solutions, best_abs_diff


def boat_monte_carlo(a, b, c, attempts=4):
    """
    Monte Carlo algoritmus:
    1) Zvolíme nízký počet pokusů (zde např. 4).
    2) V každém pokusu vygenerujeme náhodně jednu z permutací (tak, abychom ji neopakovali).
    3) Ohodnotíme její 'rating' = (váha na pravoboku) - (váha na levoboku).
    4) Pamatujeme si tu nejlepší (tj. s nejmenší absolutní hodnotou ratingu).

    Tento přístup je nedeterministický: při každém spuštění může vrátit jiný výsledek.
    """
    passengers = [a, b, c]
    used_perms = set()
    best_solution = None
    best_abs_diff = None

    for _ in range(attempts):
        # Náhodně vybereme permutaci, která ještě nebyla použita
        while True:
            perm = tuple(random.sample(passengers, 3))
            if perm not in used_perms:
                used_perms.add(perm)
                break

        left, center, right = perm
        rating = right - left

        if best_abs_diff is None or abs(rating) < best_abs_diff:
            best_abs_diff = abs(rating)
            best_solution = perm

    return best_solution, best_abs_diff


def boat_heuristic(a, b, c):
    """
    Heuristický algoritmus:
    - Využijeme symetrie: z 6 možných permutací bereme jen ty, kde (left <= right).
      Tím prohledáváme jen "polovinu" stavů.
    - Z nich vybereme ty s nejmenší absol. hodnotou ratingu.
    - Pro úplnost do výsledku přidáme i jejich "zrcadlové" varianty (right, center, left).

    Tento přístup je deterministický.
    """
    passengers = [a, b, c]
    best_solutions_half = []
    best_abs_diff = None

    # Prohledáme jen polovinu permutací (podmínka left <= right)
    for perm in itertools.permutations(passengers):
        left, center, right = perm
        if left <= right:
            rating = right - left
            if best_abs_diff is None or abs(rating) < best_abs_diff:
                best_abs_diff = abs(rating)
                best_solutions_half = [perm]
            elif abs(rating) == best_abs_diff:
                best_solutions_half.append(perm)

    # Přidáme i zrcadlové varianty
    final_solutions = set(best_solutions_half)  # set aby nedošlo k duplicitám
    for sol in best_solutions_half:
        # zrcadlo: (left, center, right) -> (right, center, left)
        mirror = (sol[2], sol[1], sol[0])
        final_solutions.add(mirror)

    return list(final_solutions), best_abs_diff


# ------------------------------------------------------------------------------
# Otestujme chování s váhami 73, 85, 81
if __name__ == "__main__":
    a, b, c = 73, 85, 81

    bf_solutions, bf_diff = boat_brute_force(a, b, c)
    print("Brute force řešení (minimální rozdíl = {}):".format(bf_diff))
    for sol in bf_solutions:
        left, center, right = sol
        rating = right - left
        print(f"  Usazení {sol}, rating = {rating}")

    mc_solution, mc_diff = boat_monte_carlo(a, b, c, attempts=4)
    print("\nMonte Carlo řešení (pokusy = 4) (rozdíl = {}):".format(mc_diff))
    left, center, right = mc_solution
    print(f"  Usazení {mc_solution}, rating = {right - left}")

    h_solutions, h_diff = boat_heuristic(a, b, c)
    print("\nHeuristické řešení (minimální rozdíl = {}):".format(h_diff))
    for sol in h_solutions:
        left, center, right = sol
        rating = right - left
        print(f"  Usazení {sol}, rating = {rating}")

"""
ROZDÍL V DETERMINISMU:
- boat_brute_force: deterministické (při stejném vstupu dostanete stejné výsledky).
- boat_monte_carlo: nedeterministické (používá se náhoda; výsledek se může lišit).
- boat_heuristic: deterministické (vždy stejný postup i výsledek).
"""
