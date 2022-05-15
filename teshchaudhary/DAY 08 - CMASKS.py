for _ in range(int(input())):
    X,Y=map(int,input().split(" "))
    if X*100>Y*10:
        print("Cloth")
    elif X*100<Y*10:
        print("Disposable")
    else:
        print("Cloth")
