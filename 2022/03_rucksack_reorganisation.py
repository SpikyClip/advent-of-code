def get_priority(item):
    """Get priority of item using ordinal offset."""
    if item.islower():
        offset = 96
    elif item.isupper():
        offset = 38

    return ord(item) - offset


def get_rucksacks(path):
    """Get list of rucksacks from path.txt"""
    with open(path) as f:
        rucksacks = f.read().splitlines()

    return rucksacks


def common_compartment_item(rucksacks):
    """
    Get the common item in both compartments using set intersection,
    returning its priorities as a list.
    """
    priorities = list()

    for rucksack in rucksacks:
        size = len(rucksack) // 2
        part_1, part_2 = set(rucksack[:size]), set(rucksack[size:])
        common = part_1.intersection(part_2).pop()
        priorities.append(get_priority(common))

    return priorities


def common_team_badge(rucksacks):
    """
    Get the common badge in teams of 3, returning its priorities as a
    list
    """
    priorities_badge = list()

    for i in range(0, len(rucksacks), 3):
        rucksack_team = [set(rucksack) for rucksack in rucksacks[i : i + 3]]
        badge = rucksack_team[0].intersection(*rucksack_team[1:3]).pop()
        priorities_badge.append(get_priority(badge))

    return priorities_badge


if __name__ == "__main__":
    path = "inputs/03_rucksack_reorganisation.txt"
    rucksacks = get_rucksacks(path)

    #
    # Part I
    #
    priorities = common_compartment_item(rucksacks)
    total = sum(priorities)
    print(total)

    #
    # Part II
    #
    priorities = common_team_badge(rucksacks)
    total = sum(priorities)
    print(total)
