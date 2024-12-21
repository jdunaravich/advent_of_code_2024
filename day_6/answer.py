import os


def main():
    input_file_contents = load_input()
    lab_map = text_to_2d_array(input_file_contents)
    total_squares_visited, outcome = plot_route(lab_map)
    print("Visited %s squares before %s" % (total_squares_visited, outcome))
    block_all_possible_spots(lab_map)

def block_all_possible_spots(lab_map):
    from collections import defaultdict
    outcomes = defaultdict(int)
    for row in range(len(lab_map)):
        for column in range(len(lab_map[0])):
            if lab_map[row][column] == ".":
                visited, outcome = plot_route_with_blocked(lab_map, row, column)
                outcomes[outcome] += 1
    print(outcomes)
    # print("Visited %s squares before %s when row %s and col %s was blocked" % (visited, outcome, row, column))


def plot_route_with_blocked(lab_map, row, column):
    replacement_lab_map = lab_map[:]
    replacement_row = replacement_lab_map[row][:]
    replacement_row[column] = "#"
    replacement_lab_map[row] = replacement_row
    return plot_route(lab_map=replacement_lab_map)


def plot_route(lab_map):
    current_row, current_column = find_dude(lab_map)
    # print("Dude is at %s row and %s column" % (current_row, current_column))
    orientation = "up"

    visited = set()
    visited_at_orientation = set()
    while True:
        visited.add((current_row, current_column))
        position_and_heading = (current_row, current_column, orientation)
        if position_and_heading in visited_at_orientation:
            return len(visited), "loop"
        visited_at_orientation.add(position_and_heading)
        if orientation == "up":
            next_row = current_row - 1
            next_column = current_column
            # Check if that's out of bounds:
            if next_row < 0:
                # print("Exited out the top!")
                return len(visited), "exited top"
            if lab_map[next_row][next_column] == '#':
                # Turn right
                orientation = "right"
                continue
            current_row, current_column = next_row, next_column
            continue
        if orientation == 'right':
            next_row = current_row
            next_column = current_column + 1
            if next_column == len(lab_map[0]):
                # print("Exited out the right!")
                return len(visited), "exited right"
            if lab_map[next_row][next_column] == '#':
                # Turn right
                orientation = "down"
                continue
            current_row, current_column = next_row, next_column
            continue
        if orientation == "down":
            next_row = current_row + 1
            next_column = current_column
            # Check if that's out of bounds:
            if next_row == len(lab_map):
                # print("Exited out the bottom!")
                return len(visited), "exit bottom"
            if lab_map[next_row][next_column] == '#':
                # Turn right
                orientation = "left"
                continue
            current_row, current_column = next_row, next_column
            continue
        if orientation == 'left':
            next_row = current_row
            next_column = current_column - 1
            if next_column < 0:
                # print("Exited out the left!")
                return len(visited), "exit left"
            if lab_map[next_row][next_column] == '#':
                # Turn right
                orientation = "up"
                continue
            current_row, current_column = next_row, next_column
            continue
    raise Exception("Damn")


def text_to_2d_array(input_file_contents):
    lab_map = [list(row) for row in input_file_contents.split('\n')]
    return lab_map


def find_dude(lab_map):
    for row in range(len(lab_map)):
        for column in range(len(lab_map[0])):
            if lab_map[row][column] == "^":
                return row, column


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
