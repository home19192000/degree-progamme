#password = 'a123456'
password = 'a123456'
i = 3
while True:
	pwd = input ('請輸入password:')
	if pwd == password:
		print('login pass!!!!!!!')
		break
	else:
		i = i - 1
		print('wrong password還有',i,'次機會')
		if i == 0:
			print('game over')
			break