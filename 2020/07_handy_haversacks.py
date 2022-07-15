# --- Day 7: Handy Haversacks ---
# https://adventofcode.com/2020/day/7

import re


def gen_bags_dict(rules):
    """
    Generates a dictionary of bag keys where values are tuples corresponding to
    the number and type of bag within
    """
    bag_dict = dict()

    # Use positive lookahead to match leading bag that will form key
    re_leading_bag = re.compile(r"(?P<col>[\w ]+) bags (?=contain)")
    # Matches inner bags that always have a number followed by colour and
    # "bag[s]" where bag may be singular (no letter 's')
    re_bags_within = re.compile(r"(?P<num>\d+) (?P<col>[\w ]+) (?=bags?)")

    for rule in rules:
        # Get the leading bag colour
        col = re_leading_bag.match(rule).group("col")
        # Match inner bags in the form of a list of tuples
        bags_within = re_bags_within.findall(rule)
        # If bag contains nothing (no re_bag_within match) supply dummy tuple
        if bags_within:
            bag_dict[col] = [(int(i), bag) for i, bag in bags_within]
        else:
            bag_dict[col] = [(0, None)]

    return bag_dict


def check_colour(bag, bag_dict, colour="shiny gold"):
    """
    Check if a bag matches the desired colour. If not, recursively look through
    its contents until it finds at least one bag of the desired colour.
    """
    if bag == colour:
        return True
    # Terminate empty bag paths
    elif bag == None:
        return False
    # Check colour of internal bags recursively, returning True if any of them
    # contain a bag of the desired colour.
    else:
        return any(
            check_colour(sub_bag, bag_dict, colour)
            for i, sub_bag in bag_dict[bag]
        )


def count_bags(leading_bag, bag_dict):
    """
    Recursively count bags within bags, considering the multiplicative number
    of bags at each level.
    """
    total = 0

    if leading_bag is not None:
        for count, bag in bag_dict[leading_bag]:
            # Recursively look into 'leading_bag's inner bags
            subcount = count_bags(bag, bag_dict)

            # If bag does contains non-empty bags (total > 0), multiply the top
            # count with subcount
            if subcount:
                total += count * subcount
            # Otherwise, just count the top level of bags
            total += count

    # Propagate 'total' recursively
    return total


if __name__ == "__main__":
    with open("inputs/07.txt") as f:
        rules = f.read().splitlines()

    # Generate bag dictionary from rules
    bag_dict = gen_bags_dict(rules)

    #
    # Part I
    #

    shiny_gold_count = 0

    # Loop through bags, ignoring the top level shiny gold bag and counting when the
    # bag does contain at least one shiny gold bag.
    for bag in bag_dict:
        if bag != "shiny gold" and check_colour(bag, bag_dict):
            shiny_gold_count += 1

    print(
        f"Part I: There are {shiny_gold_count} bags that eventually contain a 'shiny gold' bag."
    )
    #
    # Part II
    #
    bag_count = count_bags("shiny gold", bag_dict)

    print(f"Part II: a 'shiny gold' bag contains {bag_count} bags.")
