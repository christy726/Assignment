ops=int(input('''Choose string operation: \n
	1 -> Capitalize (Converts the first character to upper case)
	2 -> Lower (Converts a string into lower case)
	3 -> Swapcase (Swaps cases, lower case becomes upper case and vice versa)
	4 -> Upper -> (Converts a string into upper case)
	5 -> Encode -> (Returns an encoded version of the string)
	6 -> Partition -> (Returns a tuple where the string is parted into three parts)
	7 -> Swapcase -> (Swaps cases, lower case becomes upper case and vice versa)
	8 -> Find (Searches the string for a specified value and returns the position of where it was found)
	\n'''))

str=input("Enter your input \n")

if (ops==1):
	x=str.capitalize()
	print(x)
elif (ops==2):
	x=str.lower()
	print(x)
elif (ops==3):
	x=str.swapcase()
	print(x)
elif (ops==4):
	x=str.upper()
	print(x)
elif (ops==5):
	x=str.encode()
	print(x)
elif (ops==6):
	y=input("Enter the element to seperate : \t")
	x=str.partition(y)
	print(x)
elif (ops==7):
	x=str.swapcase()
	print(x)
elif (ops==8):
	y=input("Enter the target element: \t")
	x=str.find(y)
	print(x)
	
else:
	print("__________")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
