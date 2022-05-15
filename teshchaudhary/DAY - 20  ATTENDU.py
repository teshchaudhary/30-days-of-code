for _ in range(int(input())):
    N=int(input())
    B=input()
    Bn=[int(x) for x in str(B)]
    if((N-sum(Bn))<=30):
        print("YES")
    else:
        print("NO")
