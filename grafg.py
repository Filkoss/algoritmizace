import matplotlib.pyplot as plt

# Data z tabulky
ns = [4,5,6,7,8,9,10,11]
times = [0.000020, 0.000802, 0.000491, 0.005425, 0.028881, 0.281892, 3.500022, 38.980330]

# Vytvoříme okno grafu
plt.figure(figsize=(8, 5))

# Spojnicový graf s body
plt.plot(ns, times, marker='o', label="Měřená data")

# Popisky os a titul
plt.title("Časová složitost generování všech permutací (n!)")
plt.xlabel("Velikost pole (n)")
plt.ylabel("Doba běhu [s]")

# Mřížka a legenda
plt.grid(True)
plt.legend()

# Volitelně: použijte logaritmickou osu Y,
# ať lépe vidíte rychlý růst (odkomentujte):
#plt.yscale("log")

# Zobrazit graf
plt.show()
