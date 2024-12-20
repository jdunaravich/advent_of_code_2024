import os

def main():
    input_file_contents = load_input()
    word_search = input_to_2_dimensional_array(input_file_contents)
    # word_search = load_test_data()
    # occurrences = search_word_search(word_search=word_search)
    occurrences = search_word_search_strange(word_search)
    print("%s occurrences found" % occurrences)


def load_test_data():
    test_data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    word_search = [list(row) for row in test_data.split()]
    return word_search


def search_word_search_strange(word_search):
    occurrences = 0
    for row in range(1, len(word_search) - 1):
        for column in range(1, len(word_search[0]) - 1):
            character = word_search[row][column]
            if character == "A":
                if set([word_search[row-1][column-1], word_search[row+1][column+1]]) == set("MS") and \
                   set([word_search[row-1][column+1], word_search[row+1][column-1]]) == set("MS"):
                    occurrences += 1
    return occurrences


def search_word_search(word_search, search_term="XMAS"):
    directions = ("right", "left", "up", "down", "upleft", "upright", "downleft", "downright")
    per_direction = {direction: 0 for direction in directions}
    for row in range(len(word_search)):
        for column in range(len(word_search[0])):
            for direction in directions:
                if check_in_direction(word_search, row, column, search_term, direction):
                    per_direction[direction] += 1
    print(per_direction)
    found = sum(per_direction.values())
    return found

def check_in_direction(word_search, row, column, search_term, direction):
    if word_search[row][column] != search_term[0]:
        return False
    search_term = search_term[1:]
    if len(search_term) == 0:
        return True
    if "right" in direction:
        column += 1
    if "left" in direction:
        column -= 1
    if "up" in direction:
        row -= 1
    if "down" in direction:
        row += 1
    if column >= len(word_search[0]) or column < 0:
        return False
    if row >= len(word_search) or row < 0:
        return False
    return check_in_direction(word_search, row, column, search_term, direction)


def input_to_2_dimensional_array(input_file_contents):
    word_search = [[char for char in line]
        for line in input_file_contents.split()]
    return word_search



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
