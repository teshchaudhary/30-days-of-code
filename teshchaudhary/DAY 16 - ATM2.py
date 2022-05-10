for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in input().split():
        if(y>=int(i)):
            print(1,end="")
            y=y-int(i)
        else:
            print(0,end="")
    print()
