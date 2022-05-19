for _ in range(int(input())):
    X,Y=map(int,input().split())
    a=500-(X*2)+1000-((X+Y)*4)
    b=500-((X+Y)*2)+1000-(Y*4)
    print(max(a,b))
