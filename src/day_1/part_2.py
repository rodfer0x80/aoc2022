#!/usr/bin/env python3


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
    tops = list()
    for i in range(3):
        tops.append(0)
    top = 0

    for line in data:
        if line != "\n":
            top += int(line)
        else:
            for _top in tops:
                if top > _top:
                    tops.remove(_top)
                    tops.append(top)
                    break
            top = 0

    total = 0
    for _top in tops:
        total += _top
    return parseResult(total)


def output(res):
    sys.stdout.write(f"{res}\n")
    return 0


def main():
    output(solve(readfile()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
