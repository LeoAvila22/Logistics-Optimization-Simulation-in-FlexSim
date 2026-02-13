from ortools.sat.python import cp_model
import numpy as np

def getMinCostFlow(demandArray, capacityArray, costArray): 
    cost = np.array(costArray)
    shape = cost.shape            
    num_demand, num_capacity = shape
    demand = np.array(demandArray).reshape((num_demand,))
    capacity = np.array(capacityArray).reshape((num_capacity,))
    model = cp_model.CpModel()
    total_demand = int(demand.sum())
    X = {}
    for i in range(num_demand):
        for j in range(num_capacity):
            X[i, j] = model.NewIntVar(0, total_demand, f"X_{i}_{j}")

    for i in range(num_demand):
        model.Add(sum(X[i, j] for j in range(num_capacity)) == int(demand[i]))

    for j in range(num_capacity):
        model.Add(sum(X[i, j] for i in range(num_demand)) <= int(capacity[j]))
    model.Minimize(
        sum(int(round(cost[i, j])) * X[i, j]
            for i in range(num_demand)
            for j in range(num_capacity))
    )
    solver = cp_model.CpSolver()
    solver.parameters.random_seed = 1
    solver.parameters.num_search_workers = 1

    solver.Solve(model)
    result = []
    for i in range(num_demand):
        row = []
        for j in range(num_capacity):
            row.append(int(solver.Value(X[i, j])))
        result.append(row)

    return result