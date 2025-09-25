import sys

try:
    op1 = float(sys.argv[1])
    op = sys.argv[2]
    op2 = float(sys.argv[3])
    if op == "+":
        print(f"{op1} + {op2} = {op1 + op2}")
    elif op == "-":
        print(f"{op1} - {op2} = {op1 - op2}")
    elif op == "/":
        print(f"{op1} / {op2} = {op1 / op2}")
    elif op == "*":
        print(f"{op1} * {op2} = {op1 * op2}")
except Exception:
    print("err")
