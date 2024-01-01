from puzzle_interface import Puzzle
from queue import Queue


class Day4(Puzzle):
    def part_1(self) -> str:
        cards = parse_cards(self.input)
        point_sum = 0

        for card in cards:
            point_sum += calculate_score(card)

        return str(point_sum)

    def part_2(self) -> str:
        cards = parse_cards(self.input)
        total_cards = 0

        card_queue = Queue()
        for card in range(len(cards)):
            card_queue.put(card)

        while not card_queue.empty():
            current_card = card_queue.get()
            num_winners = count_winning_nums(cards[current_card])
            next_cards = [n for n in range(current_card + 1, current_card + num_winners + 1)]

            for card in next_cards:
                card_queue.put(card)

            total_cards += 1

        return str(total_cards)


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
    num_winning_nums = count_winning_nums(card)
    score = 0 if num_winning_nums == 0 else 2**(num_winning_nums - 1)

    return score


def count_winning_nums(card: dict[str, tuple[int, ...]]) -> int:
    num_winning_nums = 0

    for winning_num in card["winning_numbers"]:
        if winning_num in card["numbers"]:
            num_winning_nums += 1

    return num_winning_nums
