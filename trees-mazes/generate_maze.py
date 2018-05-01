import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    stack = []
    cell = random.randint(0, m.total_cells)
    visited_cells = 1

    while visited_cells < m.total_cells:
        neighbors = m.cell_neighbors(cell)
        if len(neighbors) > 0:

            neighbors_index = random.randint(0, len(neighbors) - 1)
            new_cell = neighbors[neighbors_index][0]
            compass_index = neighbors[neighbors_index][1]
            m.connect_cells(cell, new_cell, compass_index)
            stack.append(cell)
            cell = new_cell
            visited_cells += 1
        else:
            cell = stack.pop()
        m.refresh_maze_view()
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return


if __name__ == '__main__':
    main()
