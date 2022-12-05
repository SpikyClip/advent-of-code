# --- Day 2: Rock Paper Scissors ---
# https://adventofcode.com/2022/day/2

import itertools as it

with open("inputs/02_rock_paper_scissors.txt") as f:
    strat_str = f.read().splitlines()


def get_strat_guide(strat_str, outcome_known=False):
    """
    Get strategy guide and scores depending on whether the second input is
    outcome (i.e. outcome_known=True).
    """

    def remainder_to_outcome(remainder):
        """Convert remainder to outcome and points."""
        remainder_translate = {0: ("draw", 3), 1: ("win", 6), 2: ("lose", 0)}
        return remainder_translate[remainder]

    def outcome_remainder(opponent, response):
        """
        Get remainder given opponent ('A', 'B', 'C') or player response ('X',
        'Y', 'Z').
        """
        remainder = (ord(response) - ord(opponent) - 20) % 3
        return remainder

    def response_points(response):
        """Convert player response ('X', 'Y', 'Z') to points"""
        return ord(response) - 87

    def outcome_to_response(opponent, expected_outcome):
        """Convert expected outcome to respective response."""
        possible_outcomes = {
            (opponent, response): outcome_remainder(opponent, response)
            for opponent, response in it.product("ABC", "XYZ")
        }
        outcome_translate = {
            "X": ("lose", 2),
            "Y": ("draw", 0),
            "Z": ("win", 1),
        }

        expected_outcome_remainder = outcome_translate[expected_outcome][1]

        for (
            possible_opponent,
            possible_response,
        ), remainder in possible_outcomes.items():
            if (
                remainder == expected_outcome_remainder
                and possible_opponent == opponent
            ):
                return possible_response

    strat_guide = dict()
    for i, (opponent, response_or_outcome) in enumerate(
        (rnd.split() for rnd in strat_str), start=1
    ):

        if not outcome_known:
            response = response_or_outcome
        elif outcome_known:
            response = outcome_to_response(opponent, response_or_outcome)

        strat_guide[i] = {
            "opponent": opponent,
            "response": response,
            "points": remainder_to_outcome(
                outcome_remainder(opponent, response)
            )[1]
            + response_points(response),
        }

    return strat_guide


def total_score(strat_guide):
    """Return the total score given a strategy guide."""
    score = sum([strat["points"] for strat in strat_guide.values()])
    return score


#
# Part I
#

strat_guide = get_strat_guide(strat_str)
print(total_score(strat_guide))

#
# Part II
#

strat_guide = get_strat_guide(strat_str, outcome_known=True)
print(total_score(strat_guide))
