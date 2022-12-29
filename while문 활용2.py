a=1
while a<11:
	for a in range(a):
		if a%2==0:
			a+=1
		elif a%2!=0:
			print('*', end='')
			print()
