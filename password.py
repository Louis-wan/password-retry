i = 3
while True:
	password = input('please sign u password: ')
	if password == 'a123456':
		print('success')
		break
	else:
		i = i - 1
		print ('wrong ans!have', i, 'chance')

		if i == 0 :
			break
