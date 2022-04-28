for _ in range(int(input())):
    l=input().split(" ")
    M=l[0]
    W=l[1]
    i,j=0,0
    
    if len(M)>len(W):
        W,M=M,W
    
    while(i<len(M) and j<len(W)):
        if (M[i]==W[j]):
            i+=1
            j+=1
        else:
            j+=1
        
    if i==len(M):
        print("YES")
    else:
        print("NO")
