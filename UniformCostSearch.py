"""
    Let's assume V is the list of vertices and E is the dictionary of
    key = vertices and the values = a list of tuples (vertice, cost of E[i, j])
    We also assume that there is no negative weights in edges
"""

def uniformCostSearch(V, E, C, starting_vertices = None):
    # we are doing uniform cost search so our fringe is a priority queue
    fringe = PriorityQueue()
    closed = set()
    if (starting_vertices == None):
        starting_vertices = [V[0]]
    for starting_vertice in starting_vertices:
        fringe.add(starting_vertice, 0)

    while (not fringe.isEmpty()):
        vertice_to_see, cost = fringe.pop()
        closed.add(vertice_to_see)

        # do some operation on vertice

        for child_vertice, child_cost in E[vertice_to_see]:
            if (child_vertice not in closed):
                fringe.add(child_vertice, cost + child_cost)

    return
