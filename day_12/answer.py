import os


def main():
    input_string = load_input()
    garden_map = [list(item) for item in input_string.split('\n')]
    # garden_map = ["RRRRIICCFF",
    #               "RRRRIICCCF",
    #               "VVRRRCCFFF",
    #               "VVRCCCJFFF",
    #               "VVVVCJJCFE",
    #               "VVIVCCJJEE",
    #               "VVIIICJJEE",
    #               "MIIIIIJJEE",
    #               "MIIISIJEEE",
    #               "MMMISSJEEE"]
    # garden_map = ["EEEEE",
    #               "EXXXX",
    #               "EEEEE",
    #               "EXXXX",
    #               "EEEEE"]
    regions = find_regions(garden_map)
    cost = cost_of_all_regions_based_on_perimeter(regions)
    print("The total cost is %s" % cost)
    cost = cost_of_all_regions_based_on_sides(regions)
    print("The total cost based on sides is %s" % cost)


def cost_of_all_regions_based_on_sides(regions):
    running_sum = 0
    for region in regions:
        running_sum += cost_of_region_based_on_sides(region)
    return running_sum


def cost_of_region_based_on_sides(region):
    # New insight: A region has as many sides as it has corners
    sides = 0
    plots = region['plots']
    for (row, column) in plots:
        left = (row, column-1)
        right = (row, column+1)
        top = (row-1, column)
        bottom = (row+1, column)
        # Check for outer corner:
        if left not in plots and top not in plots:
            sides += 1
        if top not in plots and right not in plots:
            sides += 1
        if right not in plots and bottom not in plots:
            sides += 1
        if bottom not in plots and left not in plots:
            sides += 1
        # Check for inner corner
        topleft = (row-1, column-1)
        topright = (row-1, column+1)
        bottomright = (row+1, column + 1)
        bottomleft = (row+1, column - 1)
        if top in plots and left in plots and topleft not in plots:
            sides += 1
        if top in plots and right in plots and topright not in plots:
            sides += 1
        if bottom in plots and right in plots and bottomright not in plots:
            sides += 1
        if bottom in plots and left in plots and bottomleft not in plots:
            sides += 1
    # print("The %s region has %s sides" % (region['crop'], sides))
    return sides * len(plots)


def cost_of_all_regions_based_on_perimeter(regions):
    running_sum = 0
    for region in regions:
        running_sum += cost_of_region_based_on_permimeter(region)
    return running_sum


def cost_of_region_based_on_permimeter(region):
    fence_len = 0
    area = len(region['plots'])
    for plot in region['plots']:
        row, column = plot
        neighbors = ((row+1, column),
                     (row-1, column),
                     (row, column+1),
                     (row, column-1))
        for neighbor in neighbors:
            if neighbor not in region['plots']:
                fence_len += 1
    return fence_len * area


def find_regions(garden_map):
    all_covered = set()
    regions = []

    def add_to_region(region, row, column):
        nonlocal garden_map
        nonlocal all_covered
        if (row, column) in all_covered:
            # This is already in a region
            return
        if row < 0 or column < 0:
            return
        if row >= len(garden_map) or column >= len(garden_map[0]):
            return
        # Is this in the region?
        if garden_map[row][column] == region['crop']:
            region['plots'].add((row, column))
            all_covered.add((row, column))
            add_to_region(region, row+1, column)
            add_to_region(region, row-1, column)
            add_to_region(region, row, column+1)
            add_to_region(region, row, column-1)
        else:
            return

    for row in range(len(garden_map)):
        for column in range(len(garden_map[0])):
            if (row, column) not in all_covered:
                region = {
                    "crop": garden_map[row][column],
                    "plots": set()
                }
                add_to_region(region, row, column)
                regions.append(region)


    return regions





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
