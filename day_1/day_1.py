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
        calibration_sum = 0

        for line in self.input:
            first_digit: str
            second_digit: str

            first_digit = find_first_digit2(line)
            second_digit = find_first_digit2(line[-1::-1], reverse=True)
            calibration_num = int(first_digit + second_digit)

            calibration_sum += calibration_num

        return str(calibration_sum)


def find_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


def find_first_digit2(line: str, reverse=False) -> str:
    for idx, char in enumerate(line):
        if char.isdigit():
            return char

        num = find_number_word(line[idx:idx+5], reverse)
        if num != "":
            return num


def find_number_word(s: str, reverse: bool) -> str:
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for digit in digits:
        if not reverse and digit in s[:len(digit)]:
            return digits[digit]
        elif reverse and digit[-1::-1] in s[:len(digit)]:
            return digits[digit]

    return ""
