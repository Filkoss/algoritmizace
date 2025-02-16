import sys
import itertools
import random


def compute_rating(seating, n):
    """
    seating: list délky n (váha pasažéra nebo None).
    Vrátí rating = (váha vpravo) - (váha vlevo).
    - Pokud je n sudé, pravá = index >= n//2, levá = index < n//2.
    - Pokud je n liché, pravá = index > n//2, levá = index < n//2.
      (prostřední sedačka se nepočítá ani vpravo, ani vlevo).
    """
    mid = n // 2

    left_sum = sum(x for i, x in enumerate(seating)
                   if x is not None and i < mid)

    # pravá strana
    if n % 2 == 0:
        right_sum = sum(x for i, x in enumerate(seating)
                        if x is not None and i >= mid)
    else:
        right_sum = sum(x for i, x in enumerate(seating)
                        if x is not None and i > mid)

    return right_sum - left_sum


def boat_brute_force(weights, n):
    """
    Brute force:
    1) Vybereme 3 sedačky z n (kombinace).
    2) Zkusíme všech 6 permutací pasažérů.
    3) Vybereme uspořádání s minimálním |rating|.
    """
    best_solutions = []
    best_abs_diff = None

    for combo in itertools.combinations(range(n), 3):
        for perm in itertools.permutations(weights):
            seating = [None] * n
            seating[combo[0]] = perm[0]
            seating[combo[1]] = perm[1]
            seating[combo[2]] = perm[2]

            rating = compute_rating(seating, n)
            if best_abs_diff is None or abs(rating) < best_abs_diff:
                best_abs_diff = abs(rating)
                best_solutions = [seating]
            elif abs(rating) == best_abs_diff:
                best_solutions.append(seating)

    return best_solutions, best_abs_diff


def boat_monte_carlo(weights, n, attempts=1000):
    """
    Monte Carlo:
    - 'attempts' náhodných pokusů: vybereme 3 sedadla, pasažéry, spočítáme rating.
    - Sledujeme nejmenší |rating|.
    """
    best_seating = None
    best_abs_diff = None

    for _ in range(attempts):
        seats_chosen = random.sample(range(n), 3)
        pass_perm = random.sample(weights, 3)

        seating = [None] * n
        seating[seats_chosen[0]] = pass_perm[0]
        seating[seats_chosen[1]] = pass_perm[1]
        seating[seats_chosen[2]] = pass_perm[2]

        rating = compute_rating(seating, n)
        if best_abs_diff is None or abs(rating) < best_abs_diff:
            best_abs_diff = abs(rating)
            best_seating = seating

    return best_seating, best_abs_diff


def boat_heuristic(weights, n):
    """
    Heuristický algoritmus:
    - Např. projdeme jen kombinace i<=k, abychom vynechali "zrcadla".
    - Spočítáme rating, vybereme minima.
    - Nakonec přidáme i "zrcadlo" do setu výsledků.
    """
    best_solutions = []
    best_abs_diff = None

    for combo in itertools.combinations(range(n), 3):
        i, j, k = combo
        if i <= k:  # malé "omezení" kvůli symetrii
            for perm in itertools.permutations(weights):
                seating = [None] * n
                seating[i] = perm[0]
                seating[j] = perm[1]
                seating[k] = perm[2]

                rating = compute_rating(seating, n)
                if best_abs_diff is None or abs(rating) < best_abs_diff:
                    best_abs_diff = abs(rating)
                    best_solutions = [seating]
                elif abs(rating) == best_abs_diff:
                    best_solutions.append(seating)

    # Přidáme i "zrcadlové" varianty
    final_set = set()
    for sol in best_solutions:
        final_set.add(tuple(sol))
        mirror = tuple(reversed(sol))
        final_set.add(mirror)

    final_solutions = [list(x) for x in final_set]
    return final_solutions, best_abs_diff


def main():
    # Načteme n z příkazové řádky, jinak použijeme výchozí 5
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])
    else:
        n = 5

    print(f"Počet sedaček v lodičce: {n}")

    # Tři pasažéři
    weights = [73, 85, 81]
    print(f"Pasažéři: {weights}")

    # 1) Brute force
    bf_solutions, bf_diff = boat_brute_force(weights, n)
    print(f"\n[Brute force]\nNejmenší |rating| = {bf_diff}")
    print(f"Počet optimálních uspořádání: {len(bf_solutions)}")

    # 2) Monte Carlo
    mc_solution, mc_diff = boat_monte_carlo(weights, n, attempts=2000)
    print(f"\n[Monte Carlo]\nNejmenší |rating| = {mc_diff}")
    print("Jedno náhodně nalezené uspořádání:", mc_solution)

    # 3) Heuristika
    h_solutions, h_diff = boat_heuristic(weights, n)
    print(f"\n[Heuristický algoritmus]\nNejmenší |rating| = {h_diff}")
    print(f"Počet nalezených heuristických řešení: {len(h_solutions)}")
    if h_solutions:
        print("Ukázka jednoho řešení:", h_solutions[0])


if __name__ == "__main__":
    main()
