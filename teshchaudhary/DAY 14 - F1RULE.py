for _ in range(int(input())):
    X,Y=map(int,input().split())
    t=(X*107)/100
    if Y<=t:
        print("YES")
    else:
        print("NO")
