"""
    Let's assume V is the list of vertices and E is the dictionary of
    key = vertices and the values = a list of vertices so that E(v, u) exsists
"""

def depthFirstSearch(V, E, starting_vertices = None):
    # we are doing depth first search so our fringe is a stack
    # in python we can use a list as a stack
    fringe = []
    closed = set()
    if (starting_vertices == None):
        starting_vertices = [V[0]]
    for starting_vertice in starting_vertices:
        fringe.add(starting_vertice)

    while (not fringe.isEmpty()):
        vertice_to_see = fringe.pop()

        # do some operation on vertice

        for child_vertice in E[vertice_to_see]:
            if (child_vertice not in closed):
                fringe.add(child_vertice)
                closed.add(vertice_to_see)

    return
