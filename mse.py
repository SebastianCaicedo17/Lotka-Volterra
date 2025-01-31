import numpy as np
import lotka_volterra
import lapins_renards

def mse(list_predite, list_reel): 
    list_predite = np.array(list_predite)
    list_predite *= 1000
    list_reel = np.array(list_reel)

    mse = np.mean((list_predite - list_reel)**2)/len(list_reel)
    return mse


#print("MSE Lapins", mse(lotka_volterra.predictions(1,1,1,1),lapins_renards.lapins_reel))
#print("MSE Renards",mse(lotka_volterra.renards,lapins_renards.renards_reel))
