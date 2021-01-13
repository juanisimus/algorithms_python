
def find_lowest_cost_node(costs):
    """
    docstring
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {}

#Node start
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

#Node A
graph['a'] = {}
graph['a']['fin'] = 1

#Node B
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

#Node FIN
graph['fin'] = {}

#Cost table
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

#table for parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

#Algorithm
node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print('Total is', cost['fin'])

