import time
import os

def main():
    string_input = load_input()
    maze = make_maze(string_input)
#     string_input = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""
#     maze = make_maze(string_input)
    solve_maze(maze)


class Path(object):

    def __init__(self, position, orientation, route, maze, cost=0):
        self.position = position
        self.orientation = orientation
        self.route = route
        self.route_set = set(route)
        self.cost = cost
        self.maze = maze


    def visited(self, position):
        return position in self.route_set


    def complete(self):
        return self.maze[self.route[-1][0]][self.route[-1][1]] == 'E'

    def get_children(self):
        if self.complete():
            breakpoint()
        children = []
        # Up
        row, col = self.position
        row -= 1
        if not self.visited((row, col)) and self.maze[row][col] != '#':
            cost = self.cost
            if self.orientation == 'up':
                cost += 1
            elif self.orientation == 'down':
                cost += 2001
            else:
                cost += 1001
            path = Path(position=(row, col), orientation='up', route=self.route+[(row, col)], maze=self.maze, cost=cost)
            children.append(path)
        # Down
        row, col = self.position
        row += 1
        if not self.visited((row, col)) and self.maze[row][col] != '#':
            cost = self.cost
            if self.orientation == 'down':
                cost += 1
            elif self.orientation == 'up':
                cost += 2001
            else:
                cost += 1001
            path = Path(position=(row, col), orientation='down', route=self.route+[(row, col)], maze=self.maze, cost=cost)
            children.append(path)
        # Left
        row, col = self.position
        col -= 1
        if not self.visited((row, col)) and self.maze[row][col] != '#':
            cost = self.cost
            if self.orientation == 'left':
                cost += 1
            elif self.orientation == 'right':
                cost += 2001
            else:
                cost += 1001
            path = Path(position=(row, col), orientation='left', route=self.route+[(row, col)], maze=self.maze, cost=cost)
            children.append(path)
        # Right
        row, col = self.position
        col += 1
        if not self.visited((row, col)) and self.maze[row][col] != '#':
            cost = self.cost
            if self.orientation == 'right':
                cost += 1
            elif self.orientation == 'left':
                cost += 2001
            else:
                cost += 1001
            path = Path(position=(row, col), orientation='right', route=self.route+[(row, col)], maze=self.maze, cost=cost)
            children.append(path)
        return children




def solve_maze(maze):
    position = find_start(maze)
    orientation = 'right'
    visited = dict()
    first_path = Path(position=position, orientation=orientation, route=[position], maze=maze)
    paths = [first_path]
    completed_paths = []
    global_visited = {position: {"right": [first_path]}}

    while paths:
        new_paths = []
        for path in paths:
            extensions = path.get_children()
            for path in extensions:
                if path.complete():
                    completed_paths.append(path)
                else:
                    if path.position in global_visited:
                        if path.orientation in global_visited[path.position]:
                            if global_visited[path.position][path.orientation][0].cost > path.cost:
                                global_visited[path.position][path.orientation] = [path]
                                new_paths.append(path)
                            elif global_visited[path.position][path.orientation][0].cost == path.cost:
                                global_visited[path.position][path.orientation].append(path)
                                new_paths.append(path)
                        else:
                            global_visited[path.position][path.orientation] = [path]
                            new_paths.append(path)
                    else:
                        global_visited[path.position] = {path.orientation: [path]}
                        new_paths.append(path)
        # print("There were %s paths, %s paths continuining them have been found" % (len(paths), len(new_paths)))
        paths[:] = new_paths

    min_cost = min([path.cost for path in completed_paths])
    completed_paths = sorted(completed_paths, key=lambda path: path.cost)
    best_paths = [path for path in completed_paths if path.cost == min_cost]
    print("The minimum cost would be %s" % min_cost)
    in_best_path = set()
    for path in best_paths:
        in_best_path.update(path.route_set)
    print("A total of %s cells are in a best path" % len(in_best_path))


def find_start(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                return (row, col)



def make_maze(string_input):
    maze = []
    for row in string_input.split('\n'):
        maze.append(list(row))
    return maze


def load_input(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)

    with open(input_file_name) as input_file:
        contents = input_file.read()
    return contents


if __name__ == '__main__':
    main()
