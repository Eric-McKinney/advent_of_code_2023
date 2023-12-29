from puzzle_interface import Puzzle


class Day3(Puzzle):
    def part_1(self) -> str:
        part_num_sum = 0

        num_str = ""
        is_part_num = False
        prev_y = 0
        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char.isdigit():
                    if y != prev_y:
                        if is_part_num:
                            part_num_sum += int(num_str)

                        num_str = ""
                        is_part_num = False

                    num_str += char

                    if self.has_symbol_adjacent(x, y):
                        is_part_num = True
                else:
                    if num_str != "" and is_part_num:
                        part_num_sum += int(num_str)

                    num_str = ""
                    is_part_num = False

                prev_y = y

        return str(part_num_sum)

    def part_2(self) -> str:
        gear_ratio_sum = 0
        asterisk_coords = []

        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char == "*":
                    asterisk_coords.append((x, y))

        for x, y in asterisk_coords:
            surrounding_coords = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                                  (x - 1, y), (x + 1, y),
                                  (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

            gear = []
            part_num_str = ""
            prev_y = surrounding_coords[0][1]
            for s_x, s_y in surrounding_coords:
                if s_y != prev_y and part_num_str != "":
                    gear.append(int(part_num_str))
                    part_num_str = ""

                if self.valid_coords(s_x, s_y) and self.input[s_y][s_x].isdigit():
                    if s_x < x:
                        part_num_str = self.aggregate_number(s_x, s_y, move_right=False)
                    elif s_x == x:
                        part_num_str += self.input[s_y][s_x]
                    else:
                        part_num_str += self.aggregate_number(s_x, s_y, move_right=True)
                elif self.valid_coords(s_x, s_y) and part_num_str != "":
                    gear.append(int(part_num_str))
                    part_num_str = ""

                prev_y = s_y

            if part_num_str != "":
                gear.append(int(part_num_str))

            if len(gear) == 2:
                gear_ratio_sum += gear[0] * gear[1]

        return str(gear_ratio_sum)

    def has_symbol_adjacent(self, x: int, y: int) -> bool:
        surrounding_coords = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                              (x - 1, y), (x + 1, y),
                              (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

        for s_x, s_y in surrounding_coords:
            if self.valid_coords(s_x, s_y) and is_symbol(self.input[s_y][s_x]):
                return True

        return False

    def valid_coords(self, x: int, y: int) -> bool:
        valid_x = 0 <= x < len(self.input[0])
        valid_y = 0 <= y < len(self.input)

        return valid_x and valid_y

    def aggregate_number(self, x: int, y: int, move_right: bool) -> str:
        num_str = ""

        row = y
        col = x
        while self.valid_coords(col, row) and self.input[row][col].isdigit():
            if move_right:
                num_str += self.input[row][col]
                col += 1
            else:
                num_str = self.input[row][col] + num_str
                col -= 1

        return num_str


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "." and char != "\n"
