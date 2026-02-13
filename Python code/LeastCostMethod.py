
import numpy as np

def getMinCostFlow(demandArray, capacityArray, costArray):
    cost = np.array(costArray)
    demand = np.array(demandArray).reshape((1, cost.shape[0]))
    capacity = np.array(capacityArray).reshape((1, cost.shape[1]))
    shape = cost.shape
    X = np.zeros(shape)
    supply = capacity[0].copy()
    need = demand[0].copy()
    
    while np.sum(supply) > 0 and np.sum(need) > 0:
        available = np.logical_and(supply > 0, need[:, np.newaxis] > 0)
        temp_costs = np.where(available, cost, np.inf)
        i, j = np.unravel_index(np.argmin(temp_costs), shape)
        flow = min(need[i], supply[j])
        X[i][j] = flow
        need[i] -= flow
        supply[j] -= flow

    return X.tolist()

if __name__ == '__main__':
    demand = [10, 20, 20]
    capacity = [30, 30]
    cost = [[5, 8], [2, 5], [6, 1]]
    result = getLeastCostMethod(demand, capacity, cost)
    print(result)