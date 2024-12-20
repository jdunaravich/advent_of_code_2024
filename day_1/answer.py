import os
from collections import Counter


def main():
    left, right = get_lists_from_input()
    difference = get_difference(right, left)
    print(difference)
    similarity = get_similarity(right, left)
    print(similarity)


def get_difference(right, left):
    left.sort()
    right.sort()
    assert len(left) == len(right)
    difference = 0
    for index in range(len(left)):
        difference += abs(left[index] - right[index])
    return difference


def get_similarity(right, left):
    right_counter = Counter(right)
    similarity = 0
    for number in left:
        similarity += number * right_counter[number]
    return similarity
    

def get_lists_from_input(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)

    with open(input_file_name) as input_file:
        contents = input_file.read()
    left = []
    right = []
    for line in contents.split('\n'):
        left_num, right_num = line.split()
        left.append(int(left_num))
        right.append(int(right_num))
    return left, right


if __name__ == '__main__':
    main()
