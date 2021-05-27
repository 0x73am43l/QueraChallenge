num = int(input())
if len(str(num)) < 100:
    for i in str(num):
        a = int(i) * i
        print(i+":",a)
