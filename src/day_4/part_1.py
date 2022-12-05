#!/usr/bin/env python3


import sys
import numpy as np


def parse(data):
    data_set = list()
    for line in data:
        p0, p1 = line.split(",")

        a, b = p0.split("-")
        a, b = int(a), int(b)

        c, d = p1.split("-")
        c, d = int(c), int(d)

        xs = set()
        for i in range(a, b+1):
            xs.add(i)

        ys = set()
        for i in range(c, d+1):
            ys.add(i)

        data_set.append([xs, ys])

    return data_set


def readfile(sep="\n"):
    try:
        f = open("input.txt")
        data = f.read().split(sep)
        f.close()
    except Exception as e:
        sys.stderr.write(f"{e}\n")

    for line in data:
        if line == "":
            data.remove(line)

    return parse(data)


def parseResult(res):
    return res


def solve(data_set):
    res = 0
    for p in data_set:
        if p[0].issubset(p[1]) or p[1].issubset(p[0]):
            res += 1

    return parseResult(res)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
