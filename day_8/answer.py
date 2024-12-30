import os
from collections import defaultdict
from itertools import combinations


def main():
    input_file_contents = load_input()
    map_of_antennae = convert_to_map_of_antennae(input_file_contents)
    antenna_locations = plot_locations(map_of_antennae)
    unique_antinodes = find_unique_antinodes(locations=antenna_locations, map_of_antennae=map_of_antennae)
    print("%s distinct antinodes found." % len(unique_antinodes))
    expanded_unique_antinodes = find_unique_antinodes_expanded(locations=antenna_locations, map_of_antennae=map_of_antennae)
    print("%s distinct expanded antinodes found." % len(expanded_unique_antinodes))


def find_unique_antinodes_expanded(locations, map_of_antennae):
    antinodes = set()

    def in_bounds(coords):
        nonlocal map_of_antennae
        row, column = coords
        if row < 0 or row >= len(map_of_antennae):
            return False
        if column < 0 or column >= len(map_of_antennae[0]):
            return False
        return True

    for frequency, coordinates in locations.items():
        if len(coordinates) == 1:
            # Nothing to see here
            print('Just one antenna at %s' % frequency)
            continue
        # print('Considering frequency %s' % frequency)
        for pair in combinations(coordinates, 2):
            antinodes.add(pair[0])
            # print('Initial pair: Added %s, len now %s' % (pair[0], len(antinodes)))
            antinodes.add(pair[1])
            # print('Initial pair: Added %s, len now %s' % (pair[1], len(antinodes)))
            (row_1, col_1), (row_2, col_2) = pair
            # Add what to row 1 and col 1 to get row 2 and col 2?
            row_offset_1 = row_2 - row_1
            col_offset_1 = col_2 - col_1
            # Keep adding those to the second position
            new_pos = (row_2, col_2)
            while True:
                new_pos = (new_pos[0] + row_offset_1, new_pos[1] + col_offset_1)
                if in_bounds(new_pos):
                    antinodes.add(new_pos)
                    # print('Added %s, len now %s' % (new_pos, len(antinodes)))
                else:
                    break
            new_pos = (row_1, col_1)
            while True:
                new_pos = (new_pos[0] - row_offset_1, new_pos[1] - col_offset_1)
                if in_bounds(new_pos):
                    antinodes.add(new_pos)
                    # print('Added %s, len now %s' % (new_pos, len(antinodes)))
                else:
                    break
    return antinodes



def find_unique_antinodes(locations, map_of_antennae):
    antinodes = set()

    def in_bounds(coords):
        nonlocal map_of_antennae
        row, column = coords
        if row < 0 or row >= len(map_of_antennae):
            return False
        if column < 0 or column >= len(map_of_antennae[0]):
            return False
        return True

    for frequency, coordinates in locations.items():
        for pair in combinations(coordinates, 2):
            (row_1, col_1), (row_2, col_2) = pair
            # From A to B:
            offset_1 = ((row_1 - row_2), (col_1 - col_2))
            antinode_1 = (row_1 + offset_1[0], col_1 + offset_1[1])
            offset_2 = ((row_2 - row_1), (col_2 - col_1))
            antinode_2 = (row_2 + offset_2[0], col_2 + offset_2[1])
            if in_bounds(antinode_1):
                antinodes.add(antinode_1)
            if in_bounds(antinode_2):
                antinodes.add(antinode_2)
    return antinodes



def plot_locations(map_of_antennae):
    locations = defaultdict(list)
    for row in range(len(map_of_antennae)):
        for column in range(len(map_of_antennae[row])):
            freq = map_of_antennae[row][column]
            if freq != '.':
                locations[freq].append((row, column))
    return locations


def convert_to_map_of_antennae(input_file_contents):
    return [list(row) for row in input_file_contents.split('\n')]


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
