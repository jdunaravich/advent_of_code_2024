import os
import re


def main():
    corrupted_data = load_input()
    occurrences = find_occurrences(corrupted_data)
    print("%s occurrences in default mode" % parse_and_sum(occurrences))

    running_total = 0
    while True:
        parse_until = corrupted_data.find("don't()")
        if parse_until < 0:
            parse_until = len(corrupted_data)
        chunk = corrupted_data[:parse_until]
        running_total += parse_and_sum(find_occurrences(chunk))
        # Now try to find a new start
        if parse_until == len(corrupted_data):
            break
        corrupted_data = corrupted_data[parse_until:]
        parse_until = corrupted_data.find("do()")
        if parse_until > -1:
            corrupted_data = corrupted_data[parse_until:]
        else:
            break
    print("Running total: %s" % running_total)


def parse_and_sum(occurrences):
    total = 0
    for occurrence in occurrences:
        left, right = map(int, occurrence[4:-1].split(','))
        total += left * right
    return total


def find_occurrences(raw_input_string):
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
