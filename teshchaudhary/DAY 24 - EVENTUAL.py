for _ in range(int(input())):
    N=int(input())
    S=input()[:N]
    c=0
    for i in S:
        if S.count(i)%2!=0:
            c=1
            break
    if c==1:
        print("NO")
    else:
        print("YES")
