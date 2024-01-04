#!/usr/bin/python3
import sys


def main():
    count = 0
    length = len(sys.argv) - 1
    if length == 0:
        print("0")
        return
    else:
        for i in range(1, length + 1):
            count += int(sys.argv[i])
        print(count)


if __name__ == "__main__":
    main()
