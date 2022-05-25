a = int(input("nr1 > "))
op = input("operator > ")
b = int(input("nr2 > "))

if op == "+":
    print(a + b)
elif str(op) == "-":
    print(a - b)
elif str(op) == "/":
    print(a / b)
elif str(op) == "*":
    print(a * b)
elif str(op) == "**":
    print(a ** b)
else:
    print("Wrong value!")
