from puzzle_interface import Puzzle


class Day5(Puzzle):
    def part_1(self) -> str:
        almanac = parse_input(self.input)
        lowest_location_num = None

        for seed in almanac["seeds"]:
            soil = get_value_from_map(seed, almanac["seed-to-soil map"])
            fertilizer = get_value_from_map(soil, almanac["soil-to-fertilizer map"])
            water = get_value_from_map(fertilizer, almanac["fertilizer-to-water map"])
            light = get_value_from_map(water, almanac["water-to-light map"])
            temp = get_value_from_map(light, almanac["light-to-temperature map"])
            humidity = get_value_from_map(temp, almanac["temperature-to-humidity map"])
            location = get_value_from_map(humidity, almanac["humidity-to-location map"])

            if lowest_location_num is None or location < lowest_location_num:
                lowest_location_num = location

        return str(lowest_location_num)

    def part_2(self) -> str:
        pass


def parse_input(raw_input: list[str]) -> dict:
    almanac = {}

    seeds = [int(s) for s in raw_input[0].rstrip().split()[1:]]
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
            continue

        curr_map.append(line)

    return maps


def parse_map(m: list[str]) -> dict[int, int]:
    parsed_map = {}

    for line in m[1:]:
        line = line.rstrip().split()
        destination_range_start = int(line[0])
        source_range_start = int(line[1])
        range_len = int(line[2])

        destination_range_end = destination_range_start + range_len
        source_range_end = source_range_start + range_len

        destination_range = range(destination_range_start, destination_range_end)
        source_range = range(source_range_start, source_range_end)

        for d, s in zip(destination_range, source_range):
            parsed_map[s] = d

    return parsed_map


def get_value_from_map(key: int, m: dict[int, int]) -> int:
    if key in m:
        return m[key]

    return key
