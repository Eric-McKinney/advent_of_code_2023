import unittest
from day_3 import Day3


class MyTestCase(unittest.TestCase):
    t_input = [
        "1234*232...\n",
        "22..4...444\n",
        "*7.........\n",
        "..*.......*\n",
        "123456...45\n",
        "3*43.....2.\n",
        "4356...*..*\n",
        ".3.2...2..5\n"
    ]

    def test_aggregate_num(self):
        f_inputs = [
            (3, 0, False),
            (3, 0, True),
            (5, 0, True),
            (1, 2, True),
            (0, 1, False),
            (0, 0, True),
            (9, 4, True),
            (10, 4, True),
            (10, 4, False)
        ]
        expected_results = [
            "1234",
            "4",
            "232",
            "7",
            "2",
            "1234",
            "45",
            "5",
            "45"
        ]
        results = []

        puzzle = Day3(self.t_input)

        for f_input in f_inputs:
            x = f_input[0]
            y = f_input[1]
            move_right = f_input[2]

            results.append(puzzle.aggregate_number(x, y, move_right))

        self.assertEqual(len(expected_results), len(results))

        for idx, expected_result in enumerate(expected_results):
            self.assertEqual(expected_result, results[idx])

    def test_solve_pt2(self):
        puzzle = Day3(self.t_input)

        expected_result = 2*77 + 7*123456 + 5*2
        result = int(puzzle.part_2())

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
