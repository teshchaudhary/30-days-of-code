for _ in range(int(input())):
    N,X=map(int,input().split())
    Sn=list(map(int, input().split()))
    Sn.sort()
    if (X>Sn[N-1] or X<Sn[0]):
        print("NO")
    else:
        print("YES")
