################################################################

# Ashwini Iral Barboza

################################################################


knight_graph = {}
dfs_visited_nodes = []
dfs_found = False


# Creating the Graph
def create_graph(s, t):
    global knight_graph
    neighbours = get_neighbours(s)
    knight_graph[s] = neighbours
    for neighbour in neighbours:
        if neighbour not in knight_graph:
            create_graph(neighbour, t)


# Getting the neighbours of the 
def get_neighbours(knight_pos):
    # ascii of 'a' - 97, 'h' - 104
    neighbours = []
    knight_x, knight_y = list(knight_pos)
    knight_x_ord = ord(knight_x)
    knight_y = int(knight_y)
    if 97 <= knight_x_ord - 2 <= 104:
        if 1 <= knight_y + 1 <= 8:
            neighbours.append(chr(knight_x_ord - 2) + str(knight_y + 1))
        if 1 <= knight_y - 1 <= 8:
            neighbours.append(chr(knight_x_ord - 2) + str(knight_y - 1))
    if 97 <= knight_x_ord + 2 <= 104:
        if 1 <= knight_y + 1 <= 8:
            neighbours.append(chr(knight_x_ord + 2) + str(knight_y + 1))
        if 1 <= knight_y - 1 <= 8:
            neighbours.append(chr(knight_x_ord + 2) + str(knight_y - 1))
    if 97 <= knight_x_ord - 1 <= 104:
        if 1 <= knight_y + 2 <= 8:
            neighbours.append(chr(knight_x_ord - 1) + str(knight_y + 2))
        if 1 <= knight_y - 2 <= 8:
            neighbours.append(chr(knight_x_ord - 1) + str(knight_y - 2))
    if 97 <= knight_x_ord + 1 <= 104:
        if 1 <= knight_y + 2 <= 8:
            neighbours.append(chr(knight_x_ord + 1) + str(knight_y + 2))
        if 1 <= knight_y - 2 <= 8:
            neighbours.append(chr(knight_x_ord + 1) + str(knight_y - 2))
    return neighbours


# Travesing the graph using dfs
def dfs_traverse_graph(s, t):
    global dfs_visited_nodes, dfs_found
    dfs_visited_nodes.append(s)
    if s == t:
        dfs_found = True
        return
    for neighbour in knight_graph[s]:
        if neighbour not in dfs_visited_nodes and not dfs_found:
            dfs_traverse_graph(neighbour, t)


# Finding the paths
def find_path(s, t):
    create_graph(s, t)
    dfs_traverse_graph(s, t)
    return dfs_visited_nodes


print(find_path('a1', 'h8'))
