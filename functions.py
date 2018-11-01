# exploring functions and how to write them
# and what they do

def greeting():
	# say hello
	print("hello functioning world!")

# this is how to call on functions
greeting()

def greetings(msg="Hello Joe", num=0):
	print("Our function says", msg, "The second argument is", num)

greetings()
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)

myVariableNumber = 0


def someMath(num1=2, num2=5):
	global myVariableNumber

	myVariableNumber = num1 + num2
	return num1 + num2

sum = someMath()
print("Our sum variable is:", sum, "myVariableNumber is also:", sum)

