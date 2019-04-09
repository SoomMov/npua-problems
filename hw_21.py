a = input("input a: ")
b = input("input b: ")
c = input("input c: ")

if (c > b):
    if (c > a):
        print(c)
    else:
        print(a)
elif (b > a):
    print(b)
else:
    print(a)
