import os


def main():
    input_file_contents = load_input()
    rules, updates = input_to_rules_and_updates(input_file_contents)
    middle_sum = sum_middles_of_updates_that_follow_rules(updates, rules)
    print("Middle sum is %s" % middle_sum)
    # print(rules)
    # print("\n" * 10)
    # print(updates)


def sum_middles_of_updates_that_follow_rules(updates, rules):
    running_total = 0
    for update in updates:
        if update_follows_rules(update, rules):
            if (len(update) % 2) != 1:
                breakpoint()
            middle = update[int(len(update)/2)]
            running_total += middle
    return running_total

def update_follows_rules(update, rules):
    update_set = set(update)
    updated = set()
    for value in update:
        for precursor in rules[value]:
            if precursor in update_set and precursor not in updated:
                return False
        updated.add(value)
    return True


def input_to_rules_and_updates(input_file_contents):
    from collections import defaultdict
    rules = defaultdict(set)
    updates = []
    for line in input_file_contents.split('\n'):
        if '|' in line:
            before, after = map(int, line.split('|'))
            rules[after].add(before)
        elif ',' in line:
            updates.append(list([int(number) for number in line.split(',')]))
    return rules, updates


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
