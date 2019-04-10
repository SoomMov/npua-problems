a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

if (c == b) and (b == 2):
    if(not b == a):
        print(True)
    else:
        print(False)
elif (a == b == 2):
    if(not c == a):
        print(True)
    else:
        print(False)
elif (a == c == 2):
    if(not a == b):
        print(True)
    else:
        print(False)
