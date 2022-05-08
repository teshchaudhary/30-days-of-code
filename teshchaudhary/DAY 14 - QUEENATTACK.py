for _ in range(int(input())):
    N,X,Y=map(int,input().split())
    attack=2*(N-1)+min(X-1,Y-1)+min(X-1,N-Y)+min(N-X,Y-1)+min(N-X,N-Y)
    print(attack)
