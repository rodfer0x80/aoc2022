#!/usr/bin/env python3


import sys

#!/usr/bin/env python3


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
    return parse(data)


def parseResult(res):
    return res


def solve(data):
    top = 0
    new_top = 0
    for line in data:
        if line != "\n":
            new_top += int(line)
        else:
            if new_top > top:
                top = new_top
            new_top = 0
    return parseResult(top)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
