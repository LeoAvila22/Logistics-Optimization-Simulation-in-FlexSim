import numpy as np

def getMinCostFlow(demandArray, capacityArray, costArray):
    cost = np.array(costArray)
    demand = np.array(demandArray).reshape((1, cost.shape[0]))
    capacity = np.array(capacityArray).reshape((1, cost.shape[1]))
    shape = cost.shape

    X = np.zeros(shape)
    supply = capacity[0].copy()
    need = demand[0].copy()

    i, j = 0, 0
    while i < shape[0] and j < shape[1]:
        flow = min(need[i], supply[j])
        X[i][j] = flow
        need[i] -= flow
        supply[j] -= flow
        if need[i] == 0:
            i += 1
        if supply[j] == 0:
            j += 1

    return X.tolist()