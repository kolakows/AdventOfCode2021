from utils.data import read_lines


class Submarine:
    def __init__(self, commands):
        self.commands = commands
        self.depth = 0
        self.position = 0
        self.aim = 0

    def part1_result(self):
        # we interpreted the commands wrong and mistook the aim for the depth
        return self.position * self.aim

    def part2_result(self):
        return self.position * self.depth

    def run(self):
        for command in self.commands:
            self.interpret_command(command)

    def interpret_command(self, command):
        direction, units = command.split()
        units = int(units)
        if direction == 'up':
            self.aim -= units
        elif direction == 'down':
            self.aim += units
        elif direction == 'forward':
            self.depth += self.aim * units
            self.position += units


data_path = '../input/day2.txt'
commands = read_lines(data_path)
submarine = Submarine(commands)
submarine.run()
print(f'2-1 {submarine.part1_result()}')
print(f'2-2 {submarine.part2_result()}')
