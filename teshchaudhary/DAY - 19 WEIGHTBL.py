for _ in range(int(input())):
    w1,w2,x1,x2,M=map(int,input().split())
    diff=abs(w2-w1)
    if (diff>=x1*M) and (diff<=x2*M):
        print(1)
    else:
        print(0)
