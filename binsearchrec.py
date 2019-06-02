#Binary search program using recursion

def binary(lst,key,l,h):
	if l>h:
		return False
	else:
		k=(l+h)//2
		if key==lst[k]:
			return True
		else:
			if key>lst[k]:
				return binary(lst,key,mid+1,h)
			else:
				return binary(lst,key,l,mid-1)

