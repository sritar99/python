#linear search program in python 
def linearsearch(lst,k):
	c=0
	for i in range(len(lst)):
		if k == lst[i]:
			print("key is found! at position: ",i)
			return 
	c=1	
	if c==1:
		print("Key Not Found!")
	return 
	


s=input("Enter elements using comma : ")
l=[int(x) for x in s.split(",")]
key=int(input("Enter key to search : "))
linearsearch(l,key)
	








		