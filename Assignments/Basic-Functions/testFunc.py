"""
getValue() function
Reads an integer input from console and assigns it to a local variable.
"""

def getValue():
	value = raw_input("Enter an integer: ")
	return value

"""
validateValue() function

Validates the given value is an integer and returns it if possible.
If the value is not an integer, the program will throw an Except clause
and exit.
"""
def validateValue(value):
	try:
		x = int(value)
		return int(x)
	except:
		print "Value is not an integer."
		exit()

"""
findArea() function
Returns area for the two given variables.
"""
def findArea(var1, var2):
	return var1 * var2

