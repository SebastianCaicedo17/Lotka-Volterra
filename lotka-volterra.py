import matplotlib.pyplot as plt 

lapins = [1]
renards = [2]

alpha = 1/3
beta = 1/3
delta = 1/3
gamma = 1/3

step = 0.0001

for indice in range (1, 100_000):
    new_lapin = (lapins[-1] * (alpha - beta * renards[-1])) * step + lapins [-1]
    new_renard = (renards[-1] * (delta * lapins[-1] - gamma)) * step + renards [-1]

    lapins.append(new_lapin)
    renards.append(new_renard)

plt.figure(figsize=(6,6))
plt.plot(lapins, "b-", label='Lapins')
plt.plot(renards, "r-", label='Renards')
plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend()
plt.show()