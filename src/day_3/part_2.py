#!/usr/bin/env python3


import string
import sys


def parse(data):
    return data


def readfile(sep="\n"):
    try:
        f = open("input.txt")
        data = f.read().split(sep)
        f.close()
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    for line in data:
        if line == "":
            data.remove(line)
    
    return parse(data)


def parseResult(res):
    return res


def solve(data):
    res = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    data_dict = dict()
    i = 0
    for letter in alphabet:
        i += 1
        data_dict[letter] = i
    
    for i in range(0, len(data), 3):
        xs = list()
        for d in data[i]:
            if d in data_dict.keys() and d in data[i+1] and d in data[i+2]:
                res += data_dict[d]
                break

    return parseResult(res)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
