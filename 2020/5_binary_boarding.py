import math


def lower_half(mini, maxi):
    """
    Returns new maximum after lower half is specified
    """
    span = maxi - mini
    maxi = math.floor(maxi - span / 2)
    return maxi


def upper_half(mini, maxi):
    """
    Returns new minimum after upper half is specified
    """
    span = maxi - mini
    mini = math.ceil(mini + span / 2)
    return mini


def seat_info(pattern):
    """
    Returns the row, column, and seat id given seat binary search pattern
    """
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7

    for c in pattern:
        # lower row half
        if c == "F":
            row_max = lower_half(row_min, row_max)
        # upper row half
        elif c == "B":
            row_min = upper_half(row_min, row_max)
        # lower col half
        elif c == "L":
            col_max = lower_half(col_min, col_max)
        # upper col half
        elif c == "R":
            col_min = upper_half(col_min, col_max)

    # sanity check to see if min and max converges, not strictly necessary
    if row_min == row_max and col_min == col_max:
        # get seat_id using given formula
        seat_id = row_min * 8 + col_min

        return row_min, col_max, seat_id


if __name__ == "__main__":

    max_seat_id = 0
    seat_list = list()

    with open("inputs/5.txt") as f:
        patterns = f.read().splitlines()

    for pattern in patterns:
        row, col, seat_id = seat_info(pattern)
        # store seat info
        seat_list.append((row, col, seat_id))

        # track max seat
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    # sort seats by seat_id
    seat_list.sort(key=lambda x: x[2])

    # move through seat information across a 3 seat wide frame
    for i, seat in enumerate(seat_list[1:-2], start=1):
        frame = seat_list[i - 1 : i + 2]
        (_, _, prev_id), (_, _, mid_id), (_, _, next_id) = frame
        # gap between discrepant seats is 3 wide, 2 for normal seat frames
        if (next_id - prev_id) == 3:
            # our seat is located between mid_id and next_id (because frame will
            # detect the difference first when next_id = true next seat id)
            my_id = mid_id + 1
            # There is only one missing seat with seats ahead and behind, so
            # break
            break

    print(f"{max_seat_id=}, {my_id=}")
