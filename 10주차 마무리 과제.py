answer = input()

total = 0
current = 1

for i in answer:
	if i =='O':
		total+=current
		current+=1
	elif i=='X':
		if current>1:
			current=1
	
print(total)
