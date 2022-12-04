#!/usr/bin/env python3


import string
import sys


def parse(data):
    data_set = list()
    for line in data:
        data_set.append([line[:(len(line)//2)], line[(len(line)//2):]])
    
    return data_set


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


def solve(data_set):
    res = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    data_dict = dict()
    i = 0
    for letter in alphabet:
        i += 1
        data_dict[letter] = i
    
    for ds in data_set:
        purged = list()
        for x in ds[0]:
            for y in ds[1]:
                if x in data_dict.keys() and y == x and x not in purged:
                    res += data_dict[x]
                    purged.append(x)

    return parseResult(res)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
