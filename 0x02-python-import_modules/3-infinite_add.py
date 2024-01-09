#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv[1:]
    length = len(sys.argv) - 1
    result = 0
    if length == 0:
        print(length)
    else:
        for i in arg:
            result += int(i)
    print(result)
