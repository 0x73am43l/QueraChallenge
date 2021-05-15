x = int(input())

if x <= 100:
    for i in range(1,x+1):
        print("")
        for j in range(1,x+1):
            print(j*i,end=' ')
