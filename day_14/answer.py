import os


def main():
    string_input = load_input()
    robots = string_input_to_robots(string_input)
    map_of_counts = generate_map_of_counts(robots)
    total_count = count_in_quadrants(map_of_counts)
    print("Part 1 total: %s" % total_count)
    animate_progression(robots)


def animate_progression(robots):
    # import time
    from collections import defaultdict
    safeties = defaultdict(list)
    for step in range(10000):
    # for step in (5734, 8258):
        map_of_counts = generate_map_of_counts(robots, step=step)
        safety_score = count_in_quadrants(map_of_counts)
        safeties[safety_score].append(step)
    safest = min(safeties)
    safest_step = safeties[safest][0]
    map_of_counts = generate_map_of_counts(robots, step=safest_step)
    print("The safest one is step %s" % safest_step)
    print_map(map_of_counts)


def print_map(map_of_counts):
    for row in map_of_counts:
        print("".join([str(item) for item in row]))



def count_in_quadrants(map_of_counts):
    quad_1 = quad_2 = quad_3 = quad_4 = 0
    for row in range(len(map_of_counts)):
        for col in range(len(map_of_counts[0])):
            if row < 51:
                if col < 50:
                    quad_1 += map_of_counts[row][col]
                elif col > 50:
                    quad_2 += map_of_counts[row][col]
            elif row > 51:
                if col < 50:
                    quad_3 += map_of_counts[row][col]
                elif col > 50:
                    quad_4 += map_of_counts[row][col]
    return quad_1 * quad_2 * quad_3 * quad_4


def generate_map_of_counts(robots, step=100):
    # Assume they're all on the same map
    room_cols, room_rows = robots[0].room_cols, robots[0].room_rows
    room_map = []
    for row in range(room_rows):
        room_map.append([0] * room_cols)
    for robot in robots:
        final_col, final_row = robot.get_position_at_step(step=step)
        room_map[final_row][final_col] += 1
    return room_map

def string_input_to_robots(string_input):
    robots = []
    for line in string_input.split('\n'):
        pos_string, vel_string = line[2:].split(' v=')
        position = (int(_) for _ in pos_string.split(','))
        velocity = (int(_) for _ in vel_string.split(','))
        robot = Robot(position=position, velocity=velocity)
        robots.append(robot)
    return robots


class Robot(object):

    def __init__(self, position, velocity, room_cols=101, room_rows=103):
        self.col, self.row = position
        self.vel_col, self.vel_row = velocity
        self.room_cols = room_cols
        self.room_rows = room_rows


    def __str__(self):
        template = "p=%s,%s v=%s,%s"
        return template % (self.col, self.row, self.vel_col, self.vel_row)


    def __repr__(self):
        return self.__str__()


    def get_position_at_step(self, step):
        col_pos = (self.col + (self.vel_col * step)) % self.room_cols
        row_pos = (self.row + (self.vel_row * step)) % self.room_rows
        # print("Robot started at row: %s, col: %s" % (self.row, self.col))
        # print("Robot ended up at row: %s, col: %s" % (row_pos, col_pos))
        return col_pos, row_pos


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
