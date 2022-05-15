N=int(input())
B_Num=int(input())
l=[]
for i in range(N):
    if B_Num%(2**i)==0:
        l.append(i)
    else:
        break
print(l[-1])
