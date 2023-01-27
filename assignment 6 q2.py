def Palin(phrse):	
	l1 = list(''.join(phrse.split()))
	if l1 == list(reversed(l1)):	#can use [::-1] as well, however reversed faster
		return True 
	else:
		return False
	
	
	
inp = input('Enter a Phrase: ')
if Palin(inp):
	print("Tis a palindrome. ")
	
else: 
	print('Tis not.')
	
