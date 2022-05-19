for _ in range(int(input())):
    X,Y=map(int,input().split())
    c=0
    if X==Y:
        print(c)
    else:
        for _ in range(X,Y,8):
            c+=1
        print(c)
