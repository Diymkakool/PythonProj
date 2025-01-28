print("Calc")
print("1 add 2 minus")
def minus(x, y):
    return x - y
def add(x, y):
    return x + y

while True:

    choice = input("select your choice:")
    if choice == "1":
        num1 = float(input("number 1:"))
        num2 = float(input("number 2:"))
        print(f"{add(num1, num2)}")

    if choice == "2":
        num1 = float(input("number 1:"))
        num2 = float(input("number 2:"))
        print(f"{minus(num1, num2)}")