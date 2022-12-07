#!/usr/bin/env python3


import sys
import string


def parse(data):
    drawing = data[0].split("\n")
    drawing[0] = "    " + drawing[0]

    crates_n = int(drawing[-1].strip()[-1])
    stack_max_init_x = len(drawing) - 1

    moves = data[1].split("\n")

    stacks = [[] for _ in range(crates_n)]

    for i in range(stack_max_init_x):
        line = drawing[i]
        crates = line.replace("    ", "-").replace(" ", "").replace("[", "").replace(
            "]", "")

        for s in range(len(crates)):
            if crates[s] != "-":
                stacks[s].append(crates[s])

    stacks = [stack[::-1] for stack in stacks]

    data = list()
    data.append(stacks)
    data.append(moves)
    return data


def readfile(sep="\n"):
    try:
        f = open("input.txt")
        data = f.read().strip().split(sep)
        f.close()
    except Exception as e:
        sys.stderr.write(f"{e}\n")

    for line in data:
        if line == "":
            data.remove(line)

    return parse(data)


def parseResult(res):
    return res


def solve(data):
    res = ""
    stacks = data[0]
    moves = data[1]

    for move in moves:
        tokens = move.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        if n > 1:
            xs = list()
            for i in range(n):
                popped = stacks[src].pop()
                xs.append(popped)
            for x in xs[::-1]:
                stacks[dst].append(x)
        else:
            popped = stacks[src].pop()
            stacks[dst].append(popped)

    res = "".join([stack[-1] for stack in stacks])

    return parseResult(res)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile("\n\n")))
    return 0


if __name__ == '__main__':
    sys.exit(main())
