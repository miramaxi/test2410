import os
while True:
	site = input()

	if 'http://' in site:
		os.system('start ' + site)
		print('if')
	elif 'www.' in site:
		site = 'https://' + site
		os.system('start ' + site)
		print('elif')
	else:
		site = 'https://www.' + site
		os.system('start ' + site)
		print('else')