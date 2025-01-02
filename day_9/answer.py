import os


def main():
    # test_data = "00992111777.44.333....5555.6666.....8888.."
    # print("Checksum for test data is %s" % get_checksum(test_data))
    # return
    dense_format = load_input()
    print("Original input is %s characters" % len(dense_format))
    huge_array = to_array_format(dense_format=dense_format)
    print("Expanded that to a %s item array" % len(huge_array))
    # compressed = compress(huge_array)
    # checksum = get_checksum(compressed)
    # print("Checksum was %s" % checksum)
    compressed = fancy_compress(huge_array)
    checksum = get_checksum(compressed)
    print("Checksum was %s" % checksum)


def get_checksum(compressed):
    running_total = 0
    for index, character in enumerate(compressed):
        if character == '.':
            continue
        running_total += int(character) * index
    return running_total


def fancy_compress(huge_array):
    huge_array = huge_array[:] # Just to not morph in place
    file_ids = set(huge_array) - {'.'}
    for file_id in sorted(map(int, file_ids), reverse=True):
        file_id_string = str(file_id)
        beginning = huge_array.index(file_id_string)
        end = beginning
        for index in range(beginning, len(huge_array)):
            end = index
            if huge_array[index] != file_id_string:
                end -= 1
                break
        block_len = (end - beginning) + 1
        for index, item in enumerate(huge_array):
            if item == '.':
                if huge_array[index:index+block_len] == ['.'] * block_len:
                    free_block = index
                    break
        if free_block >= beginning:
            continue
        huge_array[beginning:beginning + block_len] = ["."] * block_len
        huge_array[free_block:free_block + block_len] = [file_id_string] * block_len
    return huge_array


def compress(huge_array):
    huge_array = huge_array[:] # Just to not morph in place
    while True:
        first_dot = huge_array.index('.')
        # K, find the last block
        for index, element in enumerate(reversed(huge_array)):
            if element != '.':
                last_file = len(huge_array) - 1 - index
                break
        if first_dot > last_file:
            print("Finished compressing")
            break
        # Now swap 'em
        huge_array[first_dot], huge_array[last_file] = huge_array[last_file], huge_array[first_dot]
    return huge_array


def to_array_format(dense_format):
    on_blank = False
    file_id = "0"
    output_array = list()
    for character in dense_format:
        number = int(character)
        if not on_blank:
            output_array += [file_id] * number
            file_id = str(int(file_id) + 1)
        else:
            output_array += ['.'] * number
        on_blank = not on_blank
    return output_array



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
