import os


def main():
    input_file_contents = load_input()
    answers_and_inputs = get_answers_and_inputs(input_file_contents)
    total_valid_answers = get_total_valid_answers(answers_and_inputs)
    print("%s is all the valid answers added together" % total_valid_answers)


def get_total_valid_answers(answers_and_inputs):
    running_total = 0
    for answer, inputs in answers_and_inputs:
        if answer_can_be_reached(answer, inputs):
            running_total += answer
    return running_total


def answer_can_be_reached(answer, inputs):
    running_sum = inputs[0]

    def can_we_get_there(running_sum, inputs):
        nonlocal answer
        if running_sum > answer:
            return False
        if len(inputs) == 0:
            return running_sum == answer
        new_input = inputs[0]
        branches = [running_sum + new_input,
                    running_sum * new_input,
                    int(str(running_sum) + str(new_input))]
        return any([can_we_get_there(branch, inputs[1:]) for branch in branches])
        # return can_we_get_there(running_sum + new_input, inputs[1:]) or can_we_get_there(running_sum * new_input, inputs[1:]) or can_we_get_there

    return can_we_get_there(running_sum, inputs[1:])


def get_answers_and_inputs(input_file_contents):
    answers_and_inputs = []
    for line in input_file_contents.split('\n'):
        answer, inputs = line.split(': ')
        answer = int(answer)
        inputs = [int(number) for number in inputs.split()]
        answers_and_inputs.append([answer, inputs])
    return answers_and_inputs

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
