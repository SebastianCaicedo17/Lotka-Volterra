import lotka_volterra
import lapins_renards
import mse

param_grid = {
    'alpha': [1/3, 2/3, 1, 4/3],
    'beta': [1/3, 2/3, 1, 4/3],
    'delta': [1/3, 2/3, 1, 4/3],
    'gamma': [1/3, 2/3, 1, 4/3]
}

def grid_search(param_grid):
    best_params = None
    best_mse_lapins =  float('inf')
    best_mse_renards =  float('inf')

    for alpha in param_grid['alpha']:
        for beta in param_grid['beta']:
            for delta in param_grid['delta']:
                for gamma in param_grid['gamma']:
                    params = {'alpha': alpha, 'beta': beta, 'delta': delta, 'gamma': gamma}
                    lapins_predits = lotka_volterra.lapins
                    renards_predits = lotka_volterra.renards
                    lapins_reels = lapins_renards.lapins_reel
                    renards_reels = lapins_renards.renards_reel
                    
                    mse_lapins = mse.mse(lapins_predits, lapins_reels)
                    mse_renards = mse.mse(renards_predits, renards_reels)
                    
                    if mse_lapins < best_mse_lapins and mse_renards < best_mse_renards:
                        best_mse_lapins = mse_lapins
                        best_mse_renards = mse_renards
                        best_params = params

    print("Meilleurs paramètres trouvés : ", best_params)
    print("Meilleur MSE lapins : ", best_mse_lapins)
    print("Meilleur MSE renards : ", best_mse_renards)
    return best_params

grid_search(param_grid)
