from puzzle_interface import Puzzle


class Day5(Puzzle):
    def part_1(self) -> str:
        pass

    def part_2(self) -> str:
        pass


def parse_input(raw_input: list[str]) -> dict:
    almanac = {}

    seeds = raw_input[0].rstrip().split()[1:]
    almanac["seeds"] = seeds

    maps = separate_maps(raw_input)
    for m in maps:
        map_name = m[0][:-2]
        almanac[map_name] = parse_map(m)

    return almanac


def separate_maps(raw_input: list[str]) -> list[list[str]]:
    maps = []
    curr_map = []
    for line in raw_input[2:]:
        if line.isspace():
            maps.append(curr_map)
            curr_map = []

        curr_map.append(line)

    return maps


def parse_map(m: list[str]) -> dict[int, int]:
    pass
