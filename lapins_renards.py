import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('C:\\Users\\sebas\\OneDrive\\Bureau\\M4-HETIC\\Développement Back Python\\FOAD-Lotka-Volterra\\populations_lapins_renards.csv')

plt.figure(figsize=(10,6))
plt.plot(df['lapin'], "b-" ,label='Lapins')
plt.plot(df['renard'], "r-", label='Renards')
plt.xlabel('Temps')
plt.ylabel('Population')
plt.legend()
plt.show()