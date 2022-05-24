for _ in range(int(input())):
    N=int(input())
    An=list(map(int,input().split()))
    c=0
    for i in range (N):
        c=c|An[i]
    print(bin(c).count('1'))
