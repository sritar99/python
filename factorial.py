#recursion demonstration using factorial in python 

def factorial(num):
	if num==0  or num ==1:
		return 1
	else:
		return factorial(num-1)*num

n=int(input("Enter a number to get Factorial: "))
print("Factorial of ",n," is : ", factorial(n))