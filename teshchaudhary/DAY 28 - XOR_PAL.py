for _ in range(int(input())):

    N=int(input())

    A=input()

    c=0

    

    for i in range (N//2):

        if A[i]!=A[N-1-i]:

            c+=1

    print((c+1)//2)
