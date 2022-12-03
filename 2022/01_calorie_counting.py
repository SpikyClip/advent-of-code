# --- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1

if __name__ == "__main__":
    #
    # Part I
    #
    with open("inputs/01_calorie_counting.txt") as f:
        all_rations = f.read()

    # Split by elf, followed by converting to int
    ration_list = [
        [int(ration) for ration in elf_ration.split("\n")]
        for elf_ration in all_rations.split("\n\n")
    ]
    sum_ration_list = [sum(elf_ration) for elf_ration in ration_list]

    most_calorie_elf = max(sum_ration_list)
    print(f"Part I: {most_calorie_elf}")

    #
    # Part II
    #
    sum_top_3_elf_calories = sum(sorted(sum_ration_list)[-3:])
    print(f"Part II: {sum_top_3_elf_calories}")
