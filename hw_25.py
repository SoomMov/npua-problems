a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

if (a + b < c):
    print(1)
elif (b + c < a):
    print(1)
elif (a + c < b):
    print(1)
else:
    print(2)
