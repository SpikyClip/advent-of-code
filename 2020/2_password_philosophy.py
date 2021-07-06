import re

filename = "2.txt"
with open(filename) as f:
    content = f.read()

pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)\n")
# pattern = re.compile(r".+\n")

entries = pattern.finditer(content)

part1_valid_no = 0
part2_valid_no = 0

for entry in entries:
    mini, maxi, letter, password = (
        int(entry.group(1)),
        int(entry.group(2)),
        entry.group(3),
        entry.group(4),
    )
    if mini <= password.count(letter) <= maxi:
        part1_valid_no += 1

    keys = [password[mini - 1], password[maxi - 1]]
    if keys.count(letter) == 1:
        part2_valid_no += 1

print(part1_valid_no)
print(part2_valid_no)