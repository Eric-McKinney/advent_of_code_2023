import sys
from puzzle_interface import Puzzle
from day_1 import day_1
from day_2 import day_2
from day_3 import day_3


DAY = 3


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
        case 2:
            puzzle = day_2.Day2(p_input)
        case 3:
            puzzle = day_3.Day3(p_input)
        case _:
            print("INVALID DAY", file=sys.stderr)
            raise SystemExit

    puzzle.solve()


if __name__ == "__main__":
    main()
