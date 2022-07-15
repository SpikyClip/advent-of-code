# --- Day 8: Handheld Halting ---
# https://adventofcode.com/2020/day/8


def run(program):
    """
    Runs program given a program dictionary. Breaks infinite loops if the same
    instruction is visited twice. If the final instruction is reached, report
    that the program is fixed.
    """
    pos, acc, index_length = (
        0,
        0,
        len(program) - 1,
    )
    visited = set()

    # terminate program when 'pos' advances past the last instruction
    while pos <= index_length:
        # If pos has been visited, infinite loop has started.
        if pos in visited:
            print(f"BREAK LOOP: {pos=},{program[pos]}, {acc=}")
            return None

        # Track visited instructions
        visited.add(pos)

        # Carry out actions
        action, val = program[pos]

        if action == "nop":
            pos += 1
        elif action == "acc":
            acc += val
            pos += 1
        elif action == "jmp":
            pos += val

    # If loop successfully ends, print info and return True
    print(f"Program fixed!: {pos=}, {acc=}, {action=}, {val=}, {list(visited)[-5:]=}")
    return True


if __name__ == "__main__":
    with open("inputs/08.txt") as f:
        lines = f.read().splitlines()
        program = {i: (l.split()[0], int(l.split()[1])) for i, l in enumerate(lines)}

    #
    # Part I
    #

    run(program)

    #
    # Part II
    #

    switch = {"nop": "jmp", "jmp": "nop"}

    # Consider only actions that are potentially broken (i.e. 'nop' or 'jmp')
    filt_program = {
        pos: (action, val)
        for pos, (action, val) in program.items()
        if action in ("nop", "jmp")
    }

    # Loop through 'nop' or 'jmp' actions, swapping them and testing if it fixes
    # the program (brute force method)
    for pos, (action, val) in filt_program.items():
        # Copy necessary to avoid modifying original
        repair_prog = program.copy()
        # Swap actions in repaired program
        repair_prog[pos] = (switch[action], val)
        # Test repaired program and break if program successfully ends.
        if run(repair_prog):
            break
