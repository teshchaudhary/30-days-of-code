for _ in range(int(input())):
    N=int(input())
    An=list(map(int,input().split()[:N]))
    
    for i in reversed(range(N)):
        if An[i]!=0:
            print(i)
            break
