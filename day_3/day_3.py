from puzzle_interface import Puzzle


class Day3(Puzzle):
    def part_1(self) -> str:
        part_num_sum = 0
        symbol_coordinates = []

        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if is_symbol(char):
                    symbol_coordinates.append((x, y))

        for x, y in symbol_coordinates:
            # same but check surrounding coords for digit before calling extract number on coords with digit
            part_num_sum += extract_number(x, y)

    def part_2(self) -> str:
        pass


def is_symbol(char: str):
    return not char.isdigit() and char != "."


def extract_number(x: int, y: int) -> int:
    pass
