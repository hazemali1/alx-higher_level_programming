#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] == "+":
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], cal.add(sys.argv[1], sys.argv[3])))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], cal.sub(sys.argv[1], sys.argv[3])))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], cal.mul(sys.argv[1], sys.argv[3])))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], cal.div(sys.argv[1], sys.argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
