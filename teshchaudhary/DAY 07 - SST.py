for _ in range(int(input())):
    A,B=map(int,input().split(" "))
    
    if A/0.1>B/0.2:
        print("FIRST")
    elif A/0.1<B/0.2:
        print("SECOND")
    else:
        print("ANY")
