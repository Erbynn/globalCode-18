def calculate():
	print("********Simple Calculator********")

	int1 = input("Enter first  number: ")
	int2 = input("Enter second number: ")
	str = input("Choose an operation(add,subtract,multiply,divide)")

	if str == "add":
		add = int1 + int2
		return add
	elif str == "subtract":
		subtract =  int1 - int2
		return subtract
	elif str == "multiply": 
		multiply = int1 * int2
		return multiply
	elif str == "divide":
		divide = int1 / int2
		return divide

calculate()


# cus inputs are taken from user make sure u dont add arguments to your fxn
