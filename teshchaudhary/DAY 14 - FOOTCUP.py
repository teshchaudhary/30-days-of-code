for _ in range(int(input())):
    X,Y=map(int,input().split())
    if X>0 and Y>0 and X==Y:
        print("YES")
    else:
        print("NO")
