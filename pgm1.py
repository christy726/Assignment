print("\t\t***TRIGNOMETRIC TABLE***\ratio")
ratio=input('''Enter Trignometric Ratio: \n
		* sin
		* cos
		* tan \n''')
angle=int(input("Enter the angle: \n"))
if (ratio=="sin" and angle==0):
	print("0")
elif(ratio=="sin" and angle==30):
	print("1/2")
elif(ratio=="sin" and angle==45):
	print("1/√2")
elif(ratio=="sin" and angle==60):
	print("√3/2")
elif(ratio=="sin" and angle==90):
	print("1")
elif(ratio=="cos" and angle==0):
	print("1")
elif(ratio=="cos" and angle==30):
	print("√3/2")
elif(ratio=="cos" and angle==45):
	print("1/√2")
elif(ratio=="cos" and angle==60):
	print("1/2")
elif(ratio=="cos" and angle==90):
	print("0")
elif(ratio=="tan" and angle==0):
	print("0")
elif(ratio=="tan" and angle==30):
	print("1/√3")
elif(ratio=="tan" and angle==45):
	print("1")
elif(ratio=="tan" and angle==60):
	print("√3")
elif(ratio=="tan" and angle==90):
	print("1")
else:
	print("______")
	

















