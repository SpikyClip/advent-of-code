# --- Day 3: Toboggan Trajectory ---
# https://adventofcode.com/2020/day/3

filename = "3.txt"

with open(filename) as f:
    plot = f.read().splitlines()


def toboggan(plot, x_inc, y_inc):

    width = len(plot[0])
    x = 0 - x_inc
    tree = 0
    new_plot = []

    for row in plot[::y_inc]:
        split_row = list(row)
        if (x + x_inc) < width:
            x += x_inc
        else:
            x = (x + x_inc) - width
        # print(x)
        if split_row[x] == "#":
            # print('tree')
            split_row[x] = "X"
            tree += 1
        else:
            split_row[x] = "O"
            # print('open')
        new_row = "".join(split_row)
        new_plot.append(new_row)

    # for row in new_plot:
    # print(row)

    return tree


x_list = [1, 3, 5, 7, 1]
y_list = [1, 1, 1, 1, 2]

tree_multiply = 1

for x_inc, y_inc in zip(x_list, y_list):
    tree_multiply *= toboggan(plot, x_inc, y_inc)

print(tree_multiply)
