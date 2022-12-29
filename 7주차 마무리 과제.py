while True:
	print("1. 더하기")
	print("2. 빼기")
	print("3. 곱하기")
	print("4. 나누기")
	print("5. 프로그램 종료")
	menu = int(input("원하는 기능의 번호를 입력하세요: "))
	
	if menu == 5:
		print("프로그램을 종료합니다.")
		break
	elif menu < 1 or menu > 5:
		print('잘못된 번호입니다.')
	else:
		n1=int(input('첫 번째 정수를 입력하세요: '))
		n2=int(input('두 번째 정수를 입력하세요: '))
		if menu == 1:
			print('%d와 %d를 더하기 연산한 결과는 %d입니다.'%(n1,n2,n1+n2))
		elif menu == 2:
			print('%d에서 %d를 빼기 연산한 결과는 %d입니다.'%(n1,n2,n1-n2))
		elif menu == 3:
			print('%d와 %d를 곱하기 연산한 결과는 %d입니다.'%(n1,n2,n1*n2))
		else:
			if n2 == 0:
				print('연산이 불가합니다.')
			else:
				print('%d를 %d로 나누기 연산한 결과는 %f입니다.'%(n1,n2,n1/n2))
