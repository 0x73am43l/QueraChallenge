#!/usr/bin/python3
num = input().split()
z1 = int(num[0])
z2 = int(num[1])
z3 = int(num[2])

if (z1 + z2 + z3 == 180 and z1 != 0 and z2 != 0 and z3 != 0):
    print("Yes")
else:
    print("No")