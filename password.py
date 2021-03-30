i = 3
while i > 0 :
	password = input('please sign u password: ')
	if password == 'a123456':
		print('success')
		break
	else:
		i = i - 1
		print ('wrong ans!have', i, 'chance')
