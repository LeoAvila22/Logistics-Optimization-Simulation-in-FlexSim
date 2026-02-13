import cvxpy as cp
import numpy as np

def getMinCostFlow(demandArray, capacityArray, costArray):
    cost = np.array(costArray, dtype=float)
    demand = np.array(demandArray, dtype=float).reshape((1, cost.shape[0]))
    capacity = np.array(capacityArray, dtype=float).reshape((1, cost.shape[1]))

    X = cp.Variable(cost.shape, name="X", integer=True)

    sOnes = np.ones((1, capacity.shape[1])) 
    tOnes = np.ones((1, demand.shape[1]))    

    constraints = [tOnes @ X <= capacity, sOnes @ X.T == demand, X >= 0]
    obj = cp.sum(cp.multiply(cost, X))
    prob = cp.Problem(cp.Minimize(obj), constraints)

    prob.solve(solver=cp.ECOS_BB, verbose=False)

    if prob.status not in ("optimal", "optimal_inaccurate"):
        raise RuntimeError(f"No optimal solution was obtained. Status: {prob.status}")

    Xv = np.array(X.value, dtype=float)

    frac = np.max(np.abs(Xv - np.rint(Xv)))  
    if frac > 1e-4:
        raise RuntimeError(f"Solution is not integer (tolerance exceeded). max_frac={frac}")

    Xv[np.abs(Xv) < 1e-6] = 0.0
    Xint = np.rint(Xv).astype(int)
    Xint[Xint < 0] = 0

    cap_res = np.max((tOnes @ Xint) - capacity)   
    dem_res = np.max(np.abs((sOnes @ Xint.T) - demand))  

    if cap_res > 0 or dem_res > 0:
        raise RuntimeError(
            f"Rounding broke feasibility. cap_violation={cap_res}, demand_violation={dem_res}"
        )
    return Xint.tolist()
