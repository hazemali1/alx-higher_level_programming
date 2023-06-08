#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    for m in range(1, len(sys.argv)):
        a += int(sys.argv[m])
    print(a)
