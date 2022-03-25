# --- Day 6: Custom Customs ---
# https://adventofcode.com/2020/day/6


def question_count(groups, mode):
    """
    Return the sum of unique questions answered per group, based on whether
    anyone answered them, or if everyone did.
    """
    if mode == "anyone":
        set_func = set.union
    elif mode == "everyone":
        set_func = set.intersection
    group_sets = list()

    for group in groups:
        person_sets = [set(person) for person in group]
        group_set = set_func(*person_sets)
        group_sets.append(group_set)

    return sum([len(group_set) for group_set in group_sets])


if __name__ == "__main__":
    with open("inputs/6.txt") as f:
        content = f.read().split("\n\n")

    groups = [group.split() for group in content]
    anyone = question_count(groups, "anyone")
    everyone = question_count(groups, "everyone")

    print(f"{anyone=}, {everyone=}")
