for _ in range(int(input())):
	l = list(map(int, input().split()))
	Parties = "ABC"
	res ="NOTA"
	for i in l:
		if i>50:
			res=Parties[l.index(i)]
	print(res)
