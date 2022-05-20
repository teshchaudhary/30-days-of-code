import math
for _ in range(int(input())):
    N,X=map(int,input().split())
    Hn=list(map(int,input().split()))
    
    sin=0
    for i in Hn:
        sin=sin+math.ceil(i/X)
        
    mul=max(Hn)
        
    print(min(sin,mul))
