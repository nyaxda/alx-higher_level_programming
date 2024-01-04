#!/usr/bin/python3
import sys


def main():
    argu = len(sys.argv) - 1
    if argu == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argu))
        for i, argument in enumerate(sys.argv):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i, argument))


if __name__ == "__main__":
    main()
