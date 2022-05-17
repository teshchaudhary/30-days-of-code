for _ in range(int(input())):
    S=input()
    l=[]
    for i in S:
        x=i.isdigit()
        if x:
            l.append(int(i))
    print(sum(l))
