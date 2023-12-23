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
