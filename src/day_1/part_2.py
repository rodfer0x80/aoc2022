#!/usr/bin/env python3


import sys


def main():
    f = open("input.txt")
    data = f.readlines()
    f.close()
    
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
    
    sys.stdout.write(f"{total}\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
