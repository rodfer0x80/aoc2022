#!/usr/bin/env python3


import sys


def main():
    f = open("input.txt")
    data = f.readlines()
    f.close()
    
    top = 0
    new_top = 0
    for line in data:
        if line != "\n":
            new_top += int(line)
        else:
            if new_top > top:
                top = new_top
            new_top = 0
    
    sys.stdout.write(f"{top}\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
