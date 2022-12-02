#!/usr/bin/env python3


import sys


def parse(data):
    _data = list()
    for line in data:
        _data.append(line.split(" "))
    return _data


def readfile(sep="\n"):
    try:
        f = open("input.txt")
        data = f.read().split(sep)
        f.close()
    except Exception as e:
        sys.stderr.write(f"{e}\n")
    return parse(data)


def rps(p):
    p1, p2 = p[0], p[1]
    alphabet = ["rock", "paper", "scissors"]
    if p1 in alphabet and p2 in alphabet:
        if p1 == "rock":
            if p2 == "paper":
                return 6+2
            elif p2 == "scissors":
                return 0+3
            else:  # p2 == "rock"
                return 3+1
        elif p1 == "paper":
            if p2 == "scissors":
                return 6+3
            elif p2 == "rock":
                return 0+1
            else:  # p2 == "paper"
                return 3+2
        else:  # p1 == "scissors"
            if p2 == "rock":
                return 6+1
            elif p2 == "paper":
                return 0+2
            else:  # p2 == "scissors
                return 3+3
    else:
        return 0


def parseResult(res):
    return res


def decodePlay(p):
    alphabet = ["A", "B", "C", "X", "Y", "Z"]
    if p[0] not in alphabet or p[1] not in alphabet:
        sys.stderr.write("Error: invalid play input\n")
        return ["", ""]
    else:
        if p[0] == "A" and p[1] == "X":
            return ["rock", "scissors"]
        elif p[0] == "A" and p[1] == "Y":
            return ["rock", "rock"]
        elif p[0] == "A" and p[1] == "Z":
            return ["rock", "paper"]
        elif p[0] == "B" and p[1] == "X":
            return ["paper", "rock"]
        elif p[0] == "B" and p[1] == "Y":
            return ["paper", "paper"]
        elif p[0] == "B" and p[1] == "Z":
            return ["paper", "scissors"]
        elif p[0] == "C" and p[1] == "X":
            return ["scissors", "paper"]
        elif p[0] == "C" and p[1] == "Y":
            return ["scissors", "scissors"]
        elif p[0] == "C" and p[1] == "Z":
            return ["scissors", "rock"]


def solve(data):
    score = 0
    for rnd in data:
        score += rps(decodePlay(rnd))
    return parseResult(score)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
