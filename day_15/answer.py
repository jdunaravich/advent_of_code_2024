import time
import os



def main():
    string_input = load_input()
    board, moves = make_board_and_moves_list(string_input=string_input)
    wide_board = make_wide(board)
    part_2(wide_board, moves)


def make_wide(board):
    wide_board = []
    for row in board:
        wide_row = []
        for character in row:
            if character == '.':
                wide_row.extend([".", "."])
            elif character == '@':
                wide_row.extend(["@", "."])
            elif character == '#':
                wide_row.extend(["#", "#"])
            elif character == 'O':
                wide_row.extend(["[", "]"])
            else:
                raise "Damn"
        wide_board.append(wide_row)
    return wide_board


def part_2(board, moves):
    print_board(board)
    move_num = 0
    for move in moves:
        # time.sleep(0.5)
        process_wide_move(move, board)
        print("Just did move %s" % move_num, end="\r")
        # time.sleep(0.05)
        move_num += 1
        print_board(board)
    print_board(board)
    running_sum = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '[':
                running_sum += (100*row) + col
    print("Total nonsense score part 2: %s" % running_sum)


def process_wide_move(move, board):
    robot_row, robot_col = 0, 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '@':
                robot_row = row
                robot_col = col
                break
    boxes = []
    def up(point):
        return point[0]-1, point[1]

    def down(point):
        return point[0]+1, point[1]

    def left(point):
        return point[0], point[1]-1

    def right(point):
        return point[0], point[1]+1

    move_funs = {
        '^': up,
        'v': down,
        '>': right,
        '<': left
    }
    target_row, target_col = move_funs[move]((robot_row, robot_col))
    targets = [(target_row, target_col)]
    while len(targets):
        new_targets = []
        new_boxes = []
        # Check for all dots
        for target_row, target_col in targets:
            if board[target_row][target_col] == '.':
                print("It was a dot")
                # Do nothing
                pass
            elif board[target_row][target_col] == ']':
                new_boxes.append(((target_row, target_col-1),(target_row, target_col)))
            elif board[target_row][target_col] == '[':
                new_boxes.append(((target_row, target_col),(target_row, target_col+1)))
            elif board[target_row][target_col] == '#':
                print("It was blocked")
                return
        if new_boxes:
            for box in new_boxes:
                left, right = box
                new_left, new_right = move_funs[move](left), move_funs[move](right)
                # set((new_left, new_right)) - set((left, right))
                new_targets.extend(set((new_left, new_right)) - set((left, right)))
        boxes.extend(new_boxes)
        targets[:] = new_targets
    boxes = set(boxes)

    if boxes:
        if move == "^":
            boxes = sorted(boxes, key=lambda box: box[0][0])
        elif move == "v":
            boxes = sorted(boxes, key=lambda box: box[0][0], reverse=True)
        elif move == "<":
            boxes = sorted(boxes, key=lambda box: box[0][1])
        elif move == ">":
            boxes = sorted(boxes, key=lambda box: box[1][1], reverse = True)
        for left, right in boxes:
            new_left, new_right = move_funs[move](left), move_funs[move](right)
            # breakpoint()
            board[new_left[0]][new_left[1]] = "["
            board[new_right[0]][new_right[1]] = "]"
            # breakpoint()
            if new_left != right:
                board[right[0]][right[1]] = "."
            if new_right != left:
                board[left[0]][left[1]] = "."
            # board[right[0]][right[1]] = "."
            # print_board(board)
            # breakpoint()

    new_robot_row, new_robot_col = move_funs[move]((robot_row, robot_col))
    board[new_robot_row][new_robot_col] = "@"
    board[robot_row][robot_col] = "."




def part_1(board, moves):
    print_board(board)
    move_num = 0
    for move in moves:
        # time.sleep(0.01)
        process_move(move, board)
        print("Just did move %s" % move_num, end="\r")
        move_num += 1
        print_board(board)
    print_board(board)
    running_sum = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'O':
                running_sum += (100*row) + col
    print("Total nonsense score: %s" % running_sum)


def process_move(move, board):
    robot_row, robot_col = 0, 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '@':
                robot_row = row
                robot_col = col
                break
    boxes = []
    def up(point):
        return point[0]-1, point[1]

    def down(point):
        return point[0]+1, point[1]

    def left(point):
        return point[0], point[1]-1

    def right(point):
        return point[0], point[1]+1

    move_funs = {
        '^': up,
        'v': down,
        '>': right,
        '<': left
    }

    target_row, target_col = move_funs[move]((robot_row, robot_col))
    while target_row >= 0 and target_col >= 0:
        if board[target_row][target_col] == '.':
            break
        elif board[target_row][target_col] == 'O':
            boxes.append((target_row, target_col))
        elif board[target_row][target_col] == "#":
            return
        target_row, target_col = move_funs[move]((target_row, target_col))
    for row, col in boxes:
        new_row, new_col = move_funs[move]((row, col))
        board[new_row][new_col] = 'O'
    new_robot_row, new_robot_col = move_funs[move]((robot_row, robot_col))
    board[new_robot_row][new_robot_col] = "@"
    board[robot_row][robot_col] = "."


def make_board_and_moves_list(string_input):
    board_str, moves_list = string_input.split('\n\n')
    board = [list(line) for line in board_str.split('\n')]
    moves_list = list("".join(moves_list.split('\n')))
    return board, moves_list


def print_board(board):
    os.system('cls')
    board_str = "\n".join(["".join(line) for line in board])
    print(board_str)


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
