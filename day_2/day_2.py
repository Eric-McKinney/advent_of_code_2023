from puzzle_interface import Puzzle


class Day2(Puzzle):
    def part_1(self) -> str:
        num_colors = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        valid_id_sum = 0

        for line in self.input:
            game_data = parse_line(line)
            game_id = int(game_data[0])
            valid_game = True

            for record in game_data[1:]:
                for cube_count in record:
                    cube_count = cube_count.split()
                    count = int(cube_count[0])
                    color = cube_count[1]

                    if count > num_colors[color]:
                        valid_game = False
                        break

            if valid_game:
                valid_id_sum += game_id

        return str(valid_id_sum)

    def part_2(self) -> str:
        power_sum = 0

        for line in self.input:
            game_data = parse_line(line)
            lowest_possible_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for record in game_data[1:]:
                for cube_count in record:
                    cube_count = cube_count.split()
                    count = int(cube_count[0])
                    color = cube_count[1]

                    if lowest_possible_cubes[color] < count:
                        lowest_possible_cubes[color] = count

            power = lowest_possible_cubes["red"]*lowest_possible_cubes["green"]*lowest_possible_cubes["blue"]
            power_sum += power

        return str(power_sum)


def parse_line(line: str) -> list[str]:
    line = line.split()
    game_id = line[1][:-1]
    game_records = " ".join(line[2:]).rstrip()
    game_records = game_records.split("; ")

    game_data = [game_id]
    for game in game_records:
        cube_counts = game.split(", ")
        game_data.append(cube_counts)

    return game_data
