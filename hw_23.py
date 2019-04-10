a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))


def checkIfOne(a, b, c):
    if (a == 1) or (b == 1) or (c == 1):
        return True
    else:
        return False


d = checkIfOne(a, b, c)

print(d)
