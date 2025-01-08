import matplotlib.pyplot as plt 

time = [0]
lapins = [1]
renards = [2]

alpha = 1/3
beta = 1/3
delta = 1/3
gamma = 1/3
step = 0.001


for indice in range (1, 1000):
    new_time = time[-1] + step
    new_lapin = (lapins[-1] * (alpha - beta * renards[-1])) * step + lapins [-1]
    new_renard = (renards[-1] * (delta * lapins[-1] - gamma)) * step + renards [-1]
    time.append(new_time)
    lapins.append(new_lapin)
    renards.append(new_renard)


plt.figure(figsize=(10,6))
plt.plot(time, lapins, "b-", label='Lapins')
plt.plot(time, renards, "r-", label='Renards')
plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend()
plt.show()