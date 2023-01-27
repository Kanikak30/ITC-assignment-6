def Perfect(digit):
	if digit <= 0: 
		print('Enter a natural no.')
		return False
	
	divs = []
	for i in range(digit,0,-1):
		if digit%i==0: divs.append(i)
	if digit*2==sum(divs): return True
	else: return False
		
a = int(input('Enter a number: '))
if(Perfect(a)):print('Perfect')
else: print('Not Perfect')
