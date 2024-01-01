from puzzle_interface import Puzzle


class Day4(Puzzle):
    def part_1(self) -> str:
        cards = parse_cards(self.input)
        point_sum = 0

        for card in cards:
            point_sum += calculate_score(card)

        return str(point_sum)

    def part_2(self) -> str:
        pass


def parse_cards(cards: list[str]) -> list[dict[str, tuple[int, ...]]]:
    parsed_cards = []

    for card in cards:
        card = card.rstrip().split()
        card = card[2:]

        winning_nums, nums = extract_nums(card)
        parsed_card = {"winning_numbers": winning_nums, "numbers": nums}

        parsed_cards.append(parsed_card)

    return parsed_cards


def extract_nums(card: list[str]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    winning_nums = []
    nums = []

    before_separator = True
    for item in card:
        if item == "|":
            before_separator = False
            continue

        if before_separator:
            winning_nums.append(int(item))
        else:
            nums.append(int(item))

    return tuple(winning_nums), tuple(nums)


def calculate_score(card: dict[str, tuple[int, ...]]) -> int:
    num_winning_nums = 0

    for winning_num in card["winning_numbers"]:
        if winning_num in card["numbers"]:
            num_winning_nums += 1

    return 2**(num_winning_nums - 1) if num_winning_nums != 0 else 0
