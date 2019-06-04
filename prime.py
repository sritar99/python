import math
def isprime(num):
	if num <2:
		return False
	else:
		for i in range(2,int(math.sqrt(num))+1):
			if num%i==0:
				return False
		else:
			return True



for i in range(20):
	print(i," :",isprime(i))
