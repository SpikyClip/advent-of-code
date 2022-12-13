# --- Day 4: Camp Cleanup ---
# https://adventofcode.com/2022/day/3


def get_section_assignments(path):
    """Parse input text file and split into list of integers."""
    with open(path) as f:
        pairs = f.read().splitlines()

    section_assignment = [
        [
            [int(x) for x in section_range.split("-")]
            for section_range in pair.split(",")
        ]
        for pair in pairs
    ]

    return section_assignment


def check_sections(section_assignments, check="subset"):
    """
    Check if section assignments are subsets or intersections based on
    check value ('subset', 'intersection')
    """
    count = 0

    for pair in section_assignments:
        (p1_i, p1_n), (p2_i, p2_n) = pair
        p1_set = set(range(p1_i, p1_n + 1))
        p2_set = set(range(p2_i, p2_n + 1))

        if check == "subset":
            if p1_set.issubset(p2_set) or p2_set.issubset(p1_set):
                count += 1

        elif check == "intersection":
            if p1_set.intersection(p2_set):
                count += 1

    return count


if __name__ == "__main__":
    path = "inputs/04_camp_cleanup.txt"
    section_assignments = get_section_assignments(path)

    #
    # Part I
    #
    print(check_sections(section_assignments, check="subset"))

    #
    # Part II
    #
    print(check_sections(section_assignments, check="intersection"))
