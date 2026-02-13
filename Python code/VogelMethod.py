import numpy as np

def getMinCostFlow(demandArray, capacityArray, costArray):
    cost = np.array(costArray)
    demand = np.array(demandArray).reshape((1, cost.shape[0]))
    capacity = np.array(capacityArray).reshape((1, cost.shape[1]))
    shape = cost.shape

    X = np.zeros(shape)
    supply = capacity[0].copy()
    need = demand[0].copy()

    row_mask = np.ones(shape[0], dtype=bool)
    col_mask = np.ones(shape[1], dtype=bool)

    while np.any(row_mask) and np.any(col_mask):
        active_rows = np.where(row_mask)[0]
        active_cols = np.where(col_mask)[0]
        if len(active_rows) == 0 or len(active_cols) == 0:
            break

        active_costs = cost[np.ix_(active_rows, active_cols)]

        row_penalties = []
        for r_idx in range(len(active_rows)):
            sorted_costs = np.sort(active_costs[r_idx])
            row_penalties.append(sorted_costs[1] - sorted_costs[0] if len(sorted_costs) > 1 else float("inf"))

        col_penalties = []
        for c_idx in range(len(active_cols)):
            sorted_costs = np.sort(active_costs[:, c_idx])
            col_penalties.append(sorted_costs[1] - sorted_costs[0] if len(sorted_costs) > 1 else float("inf"))

        if max(row_penalties) >= max(col_penalties):
            r = active_rows[row_penalties.index(max(row_penalties))]
            c = np.where(col_mask)[0][np.argmin(cost[r, col_mask])]
        else:
            c = active_cols[col_penalties.index(max(col_penalties))]
            r = np.where(row_mask)[0][np.argmin(cost[row_mask, c])]

        flow = min(need[r], supply[c])
        X[r][c] = flow
        need[r] -= flow
        supply[c] -= flow

        if need[r] == 0:
            row_mask[r] = False
        if supply[c] == 0:
            col_mask[c] = False

    return X.tolist()