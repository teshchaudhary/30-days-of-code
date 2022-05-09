for _ in range(int(input())):
    N=int(input())
    c=1
    while(c*2<=N):
        c=c*2
    x=c//2
    b=x
    a=N-c+1
    print(max(a,b))
