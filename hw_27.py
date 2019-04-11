a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

if (c == b + a):
    print(True)

elif (b == c + a):
    print(True)

elif (a == b + c):
    print(True)

else:
    print(False)
