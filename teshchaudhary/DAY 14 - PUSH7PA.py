def pushpa(Hn):
    Hn.sort()
    if N==1:
        print(Hn[0])
    else:
        max=0
        c=0
        for i in range(N-1,1,-1):
            if Hn[i]==Hn[i-1]:
                c+=1
            else:
                if max<Hn[i]+c:
                    max=Hn[i]+c
                    c=0
        print(max)

for _ in range(int(input())):
    N=int(input())
    Hn = list(map(int,input().split()))
    pushpa(Hn)
