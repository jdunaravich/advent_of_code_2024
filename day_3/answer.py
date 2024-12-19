import os
import re


def main():
    corrupted_data = load_input()
    occurrences = find_instances(corrupted_data)
    print("%s occurrences" % parse_and_sum(occurrences))


def parse_and_sum(occurrences):
    total = 0
    for occurrence in occurrences:
        left, right = map(int, occurrence[4:-1].split(','))
        total += left * right
    return total



def find_instances(raw_input_string):
    occurrences = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', raw_input_string)
    return occurrences


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
