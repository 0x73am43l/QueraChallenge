s = 0
def sums(num,s):
    for digit in str(num):
        s += int(digit)
    if s < 10:
        print(s)
    else:
        for i in str(s):
            x = s % 10
            y = s // 10
            s = x + y
        print(s)

num = int(input())
if num >= 10:
    sums(num,s)
else:
    print(num)
