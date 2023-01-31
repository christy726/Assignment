list=[int(i) for i in input("Enter elements:\t").split()]
print(list)
list.sort()
tar=int(input("Enter the target element: "))
print(tar)
for i in range(len(list)):
	if(list[i]==tar):
		print("Target element",tar," is found at ",i+1,"th position")
	
