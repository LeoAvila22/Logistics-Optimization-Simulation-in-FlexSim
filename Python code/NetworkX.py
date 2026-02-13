import numpy as np
import networkx as nx

def getMinCostFlow(demandArray, capacityArray, costArray):
    cost = np.array(costArray)
    num_demand, num_capacity = cost.shape  
    demand = np.array(demandArray, dtype=int).reshape((num_demand,))
    capacity = np.array(capacityArray, dtype=int).reshape((num_capacity,))

    total_demand = int(demand.sum())
    total_capacity = int(capacity.sum())
    G = nx.DiGraph()

    for j in range(num_capacity):
        G.add_node(f"F{j}", demand=-int(capacity[j]))

    for i in range(num_demand):
        G.add_node(f"W{i}", demand=int(demand[i]))

    if total_capacity > total_demand:
        extra = total_capacity - total_demand
        G.add_node("DUMP", demand=extra)
        for j in range(num_capacity):
            G.add_edge(f"F{j}", "DUMP", capacity=int(capacity[j]), weight=0)

    big_cap = max(total_demand, total_capacity)
    for i in range(num_demand):
        for j in range(num_capacity):
            G.add_edge(f"F{j}", f"W{i}", capacity=big_cap, weight=int(round(cost[i, j])))

    total_cost, flow_dict = nx.network_simplex(G)
    result = []
    for i in range(num_demand):
        row = []
        wi = f"W{i}"
        for j in range(num_capacity):
            fj = f"F{j}"
            row.append(int(flow_dict[fj].get(wi, 0)))
        result.append(row)

    return result