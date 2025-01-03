import os


def main():
    string_input = load_input()
    as_array = convert_to_array(string_input)
    array_at_step = as_array
    # Brute force for part 1
    for iteration in range(25):
        array_at_step = run_step(array_at_step)
    print("Final 25 array is %s long" % len(array_at_step))
    total_len = efficient_iterate(as_array)
    print("Final 75 array is %s long" % total_len)


def efficient_iterate(array):
    from collections import Counter, defaultdict
    counter = dict(Counter([int(item) for item in array]))
    for iteration in range(75):
        new_counter = defaultdict(int)
        for item in counter:
            occurrences = counter[item]
            children = get_step(item)
            for child in children:
                new_counter[child] += occurrences
        counter = new_counter
        print("At iteration %s list is now %s long" % (iteration + 1, sum(counter.values())))
    return sum(counter.values())


class memoize:
    def __init__(self, function):
        self.function = function
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.function(*args)
        return self.memo[args]


@memoize
def get_step(item):
    if item == 0:
        return [1]
    if len(str(item)) % 2 == 0:
        item = str(item)
        return_array = [int(item[:int(len(item)/2)]), int(item[int(len(item)/2):])]
        return return_array
    return [item * 2024]


def run_step(array):
    new_array = []
    for item in array:
        if item == 0:
            new_array.append(1)
        elif len(str(item)) % 2 == 0:
            item = str(item)
            new_array.append(int(item[:int(len(item)/2)]))
            new_array.append(int(item[int(len(item)/2):]))
        else:
            new_array.append(item * 2024)
    return new_array


def convert_to_array(string_input):
    return [int(thing) for thing in string_input.split(' ')]


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
