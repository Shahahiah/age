driving = input('Have you ever drive a car?')
if driving != 'yes' and driving != 'no':
	print('You may only enter yes/no')
	raise SystemExit
	
age = input('What is your age?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('You passed the test')
	else:
		print('Strange why would you ever drive a car')
elif driving == 'no':
	if age >= 18:
		print('You are old enough to get a driving license, go get it')
	else:
		print('very well, after a few years time, you may go to get a driving license')
