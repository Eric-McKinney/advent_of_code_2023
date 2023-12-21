import sys
from day_1 import day_1


DAY = 1


class Puzzle:
    input: list[str]

    def __init__(self, puzzle_input: list[str]):
        self.input = puzzle_input

    def solve(self) -> None:
        print(f"Part 1: {self.part_1()}")
        print(f"Part 2: {self.part_2()}")

    def part_1(self) -> str:
        raise NotImplementedError

    def part_2(self) -> str:
        raise NotImplementedError


def read_puzzle_input() -> list[str]:
    with open(f"day_{DAY}/input.txt", "r") as f:
        p_input = f.readlines()

    return p_input


def main():
    puzzle: Puzzle
    p_input = read_puzzle_input()

    match DAY:
        case 1:
            puzzle = day_1.Day1(p_input)
        case _:
            print("INVALID DAY", file=sys.stderr)
            raise SystemExit

    puzzle.solve()


if __name__ == "__main__":
    main()
