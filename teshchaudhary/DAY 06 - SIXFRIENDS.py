T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    dub=3*X
    trip=2*Y
    print(min(dub,trip))
