# --- Day 4: Passport Processing ---
# https://adventofcode.com/2020/day/4

import re


def passport_str_to_dict(passport_str):
    """
    Converts a string passport into a dict
    """
    passport_dict = {
        key: value
        for key, value in [pair.split(":") for pair in passport_str.split()]
    }
    return passport_dict


def fields_present(passport_dict):
    """
    Checks if necessary fields are present, returning a boolean

    All passports with 8 fields are valid, all passports with less than 7
    fields are invalid, and all passports with exactly 7 fields are only valid
    if the missing field is "cid"
    """
    if len(passport_dict) == 8:
        return True

    elif (len(passport_dict) == 7) and "cid" not in passport_dict:
        return True

    else:
        return False


def fields_valid(passport_dict):
    """
    Checks if present fields are valid
    """

    # dict of lambda functions corresponding to fields that test for validity
    cond_dict = {
        "byr": (lambda byr: 1920 <= byr <= 2002),
        "iyr": (lambda iyr: 2010 <= iyr <= 2020),
        "eyr": (lambda eyr: 2020 <= eyr <= 2030),
        "hgt": (
            lambda hgt: (150 <= hgt[0] <= 193)
            if hgt[1] == "cm"
            else (59 <= hgt[0] <= 76)
        ),
        "hcl": (
            lambda hcl: True if re.match(r"\#[0-9a-f]{6}", hcl, re.I) else False
        ),
        "ecl": (
            lambda ecl: ecl.lower()
            in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        ),
        "pid": (lambda pid: True if re.match(r"\d{9}$", pid) else False),
        "cid": (lambda cid: True),
    }

    # Loop through key value pairs to test validity against cond_dict
    for key, value in passport_dict.items():
        # Sanitising of ints and discarding passports with ValueErrors
        if key in ("byr", "iyr", "eyr"):
            try:
                value = int(value)
            except ValueError:
                return False
        # Sanitising of height and unit pairs before testing
        elif key == "hgt":
            match = re.match(r"(?P<hgt>\d+)(?P<unit>cm|in)", value)
            if match:
                value = (int(match.group("hgt")), match.group("unit"))
            else:
                return False

        # If field fails test, break and move to next passport
        if not cond_dict[key](value):
            return False

    return True


if __name__ == "__main__":
    filename = "inputs/04.txt"
    valid_passport_count = 0

    with open(filename) as f:
        passports = f.read().split("\n\n")

    for passport_str in passports:
        passport_dict = passport_str_to_dict(passport_str)
        if fields_present(passport_dict) and fields_valid(passport_dict):
            valid_passport_count += 1

    print(f"There are '{valid_passport_count}' valid passports.")
