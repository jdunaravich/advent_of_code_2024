import os


def main():
    raw_data = load_input()
    games = raw_data_to_games(raw_data)
    # # Make a test game
    # button_a = Button("A", 94, 34)
    # button_b = Button("B", 22, 67)
    # prize = Prize(8400, 5400)
    # test_game = Game(button_a, button_b, prize)
    # a_freq, b_freq = test_game.button_frequencies_to_prize()
    running_total = 0
    for game in games:
        running_total += game.get_cost_in_tokens()
    print("In total it costs %s tokens to win every game Part 1" % running_total)
    running_total = 0
    for game in games:
        game.prize.x += 10000000000000
        game.prize.y += 10000000000000
        running_total += game.get_cost_in_tokens()
    print("In total it costs %s tokens to win every game Part 2" % running_total)



class Game(object):

    def __init__(self, button_a, button_b, prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize


    def __repr__(self):
        template = "Button A: X+%s, Y+%s\nButton B: X+%s, Y+%s\nPrize: X=%s, Y=%s"
        return template % (self.button_a.x, self.button_a.y,
                           self.button_b.x, self.button_b.y,
                           self.prize.x, self.prize.y)


    def button_frequencies_to_prize(self):
        """
            Button A: X+94, Y+34
            Button B: X+22, Y+67
            Prize: X=8400, Y=5400
            self.button_a.x * A + self.button_b.x * B = self.prize.x
            self.button_a.y * A + self.button_b.y * B = self.prize.y

            |self.button_a.x  self.button_b.x||A| |self.prize.x|
            |                                || |=|            |
            |self.button_a.y  self.button_b.y||B| |self.prize.y|
            TODO: Check for a zero determinant
            determinant = (self.button_a.x*self.button_b.y) - (self.button_a.y*self.button_b.x)
            A = ((self.prize.x * self.button_b.y) - (self.prize.y * self.button_a.y)) / determinant
            B = ((self.prize.x * self.button_b.x) - (self.prize.y * self.button_a.x)) / determinant
        """
        determinant = (self.button_a.x*self.button_b.y) - (self.button_a.y*self.button_b.x)
        A = ((self.prize.x * self.button_b.y) - (self.prize.y * self.button_b.x)) / determinant
        B = ((self.prize.x * self.button_a.y) - (self.prize.y * self.button_a.x)) / determinant
        try:
            assert (A % 1) == 0
            assert (B % 1) == 0
        except:
            # print("I don't think this has a solution:")
            # print(self)
            # print("\n")
            return 0, 0
            # breakpoint()
        a_freq = int(abs(A))
        b_freq = int(abs(B))
        projected_prize_x = (a_freq * (self.button_a.x)) + (b_freq * (self.button_b.x))
        projected_prize_y = (a_freq * (self.button_a.y)) + (b_freq * (self.button_b.y))
        assert projected_prize_x == self.prize.x
        assert projected_prize_y == self.prize.y
        # print("Correctly handled this game:")
        # print(self)
        # print('\n')
        return a_freq, b_freq


    def get_cost_in_tokens(self):
        a_freq, b_freq = self.button_frequencies_to_prize()
        # if (a_freq + b_freq) > 100:
        #     # Turns out this is just bullshit?
        #     return 0
        cost_in_tokens = (a_freq * 3) + (b_freq * 1)
        return cost_in_tokens


class Prize(object):

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


    def __repr__(self):
        return "Prize at %s,%s" % (self.x, self.y)


class Button(object):

    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return "Button letter: %s at %s,%s" % (self.letter, self.x, self.y)

def raw_data_to_games(raw_data):
    games = []

    for section in raw_data.split('\n\n'):
        button_a_str, button_b_str, prize_str = section.split('\n')
        x, y = button_a_str[len("Button A: X+"):].split(', Y+')
        button_a = Button(letter='A', x=x, y=y)
        x, y = button_b_str[len("Button B: X+"):].split(', Y+')
        button_b = Button(letter='B', x=x, y=y)
        x, y = prize_str[len("Prize: X="):].split(', Y=')
        prize = Prize(x=x, y=y)
        game = Game(button_a=button_a, button_b=button_b, prize=prize)
        games.append(game)
    return games


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
