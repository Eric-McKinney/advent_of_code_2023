from main import Puzzle


class Day1(Puzzle):
    def part_1(self) -> str:
        calibration_sum = 0

        for line in self.input:
            first_digit: str
            second_digit: str

            first_digit = find_first_digit(line)
            second_digit = find_first_digit(line[-1::-1])
            calibration_num = int(first_digit + second_digit)

            calibration_sum += calibration_num

        return str(calibration_sum)

    def part_2(self) -> str:
        pass


def find_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char
