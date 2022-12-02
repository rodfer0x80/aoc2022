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


def rps(p1, p2):
    alphabet = ["rock", "paper", "scissors"]
    if p1 in alphabet and p2 in alphabet:
        if p1 == "rock":
            if p2 == "paper":
                return 6+2
            elif p2 == "scissors":
                return 0+3
            else: # p2 == "rock"
                return 3+1
        elif p1 == "paper":
            if p2 == "scissors":
                return 6+3
            elif p2 == "rock":
                return 0+1
            else: # p2 == "paper"
                return 3+2
        else: # p1 == "scissors"
            if p2 == "rock":
                return 6+1
            elif p2 == "paper":
                return 0+2
            else: # p2 == "scissors
                return 3+3
    else:
        return -1

def parseResult(res):
    return res

def decodePlay(p):
    alphabet = ["A", "B", "C", "X", "Y", "Z"]
    if p not in alphabet:
        return ""
    else:
        if p == "A" or p == "X":
            return "rock"
        elif p == "B" or p == "Y":
            return "paper"
        else:
            return "scissors"


def solve(data):
    score = 0
    for rnd in data:
        score += rps(decodePlay(rnd[0]), decodePlay(rnd[1]))
    return parseResult(score)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
