import copy

import regex as re


def process_input(path):
    """
    Processes path input to return a diagram dict and list of tuple moves.
    """

    def diagram_to_dict(diagram):
        """Converts a diagram str to dict."""
        col_idx = [int(x) for x in list(diagram[-1]) if x != " "]
        diagram_dict = {i: list() for i in col_idx}

        for row in diagram[-2::-1]:
            row_crates = row[1::4]

            for crate, col in zip(row_crates, diagram_dict.keys()):
                if crate.isalpha():
                    diagram_dict[col].append(crate)

        return diagram_dict

    def moves_to_tuple(moves):
        """Converts a moves str to a list of tuples."""
        tuple_moves = list()
        pattern = re.compile(
            r"move (?P<n>\d+) from (?P<from>\d+) to (?P<to>\d+)"
        )

        moves = (pattern.match(move) for move in content[idx + 1 :])
        for move in moves:
            tuple_move = tuple(int(x) for x in move.group("n", "from", "to"))
            tuple_moves.append(tuple_move)

        return tuple_moves

    with open(path) as f:
        content = f.read().splitlines()

    idx = content.index("")
    diagram = content[:idx]
    moves = content[idx + 1 :]

    diagram_dict = diagram_to_dict(diagram)
    tuple_moves = moves_to_tuple(moves)

    return (diagram_dict, tuple_moves)


def move_crates(diagram_dict, moves, cratemover=9000):
    """
    Moves crates one by one or multiple at a time depending on cratemover value
    (9000, 9001). Returns new diagram_dict.
    """
    moved_diagram_dict = copy.deepcopy(diagram_dict)

    for move in moves:
        n, frm, to = move

        if cratemover == 9000:
            for i in range(1, n + 1):
                frm_crate = moved_diagram_dict[frm].pop()
                moved_diagram_dict[to].append(frm_crate)

        elif cratemover == 9001:
            frm_crate = moved_diagram_dict[frm][-n:]
            moved_diagram_dict[to].extend(frm_crate)
            del moved_diagram_dict[frm][-n:]

    return moved_diagram_dict


def get_top_crates(diagram_dict):
    """Gets the top crates and joins them into one string."""
    top_crates = [col[-1] for col in diagram_dict.values()]
    return "".join(top_crates)


if __name__ == "__main__":
    path = "inputs/05_supply_stacks.txt"
    diagram_dict, moves = process_input(path)

    #
    # Part I
    #
    moved_diagram_dict = move_crates(diagram_dict, moves, cratemover=9000)
    print(get_top_crates(moved_diagram_dict))

    #
    # Part II
    #
    moved_diagram_dict = move_crates(diagram_dict, moves, cratemover=9001)
    print(get_top_crates(moved_diagram_dict))
