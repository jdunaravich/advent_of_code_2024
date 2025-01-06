import os


def main():
    input_data = load_input()
    terrain_map = get_2d_array(input_data)
    paths = find_all_paths(terrain_map=terrain_map)
    print("There are %s paths" % len(paths))
    score = get_total_score(paths)
    print("The total score is %s" % score)


def get_total_score(paths):
    from collections import defaultdict
    scores = defaultdict(set)
    for path in paths:
        scores[path[0]].add(path[-1])
    running_sum = 0
    for start in scores:
        running_sum += len(scores[start])
    return running_sum


def find_all_paths(terrain_map):
    paths = []
    for row in range(len(terrain_map)):
        for column in range(len(terrain_map[0])):
            if terrain_map[row][column] == 0:
                paths.extend(find_paths(terrain_map=terrain_map, path_so_far=[], row=row, column=column))
    return paths



def find_paths(terrain_map, path_so_far, row, column):
    if row < 0 or column < 0:
        return []
    if row >= len(terrain_map) or column >= len(terrain_map[0]):
        return []
    # Check that this is a valid step
    if len(path_so_far) == 0:
        previous_value = -1
    else:
        last_row, last_col = path_so_far[-1]
        previous_value = terrain_map[last_row][last_col]

    if previous_value + 1 == terrain_map[row][column]:
        if terrain_map[row][column] == 9:
            # Finished a path
            finished_path = path_so_far[:]
            finished_path.append((row, column))
            return [finished_path]
        new_path = path_so_far + [(row, column)]
        extended_paths = find_paths(terrain_map=terrain_map, path_so_far=new_path, row=row-1, column=column) + \
               find_paths(terrain_map=terrain_map, path_so_far=new_path, row=row+1, column=column) + \
               find_paths(terrain_map=terrain_map, path_so_far=new_path, row=row, column=column-1) + \
               find_paths(terrain_map=terrain_map, path_so_far=new_path, row=row, column=column+1)
        return extended_paths
    return []


def get_2d_array(input_data):
    as_array = [[int(character) for character in line] for line in input_data.split('\n')]
    return as_array


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
