##Variable
num1 = 1
##Python Data Types:
Integer = 9
Float = 9.01
String = "Dagul"
String1 = "3"
List = ['Dagul', 'nognog']
Tuple = (1, 2, 3, 'a', 'b', 'c')
Dictionary = {
	'index1': 'value1',
	'index2': 'value2'
}
Boolean = True
##alt + p = repeat the last command in python
##Built-in functions:
print(type(num1)) ##get the datatype
len(Tuple) ##count each element inside variable
print("Hello {}, ukininam!".format(String)) ##String format
print(int(String1) + num1)##implicitly change String1 to int data type
##Python treats collection objects such as List, Tuple, Set, and the Dictionary as an ARRAY.
##String dataType is considered as an array or tuple data types
List.append("densha")##add an element inside a list
##Tuple is immutable, once set can no longer change
##Converting Tuple to List type:
animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox' )
lstAnimal = list(animal)
print(lstAnimal)
##Converting String to List type(by elements):
myString = "Hello I am pleased to meet you"
newString = list(myString)
print(newString)
##Converting String to List type(by words):
newString = myString.split(" ")
print(newString)
##Check built-in helper methods:
help(str)
help(dict)
help(list)
help(int)
help(set)
help(float)
help(tuple)
help(bool)
##Dictionary in Python is like an object in JavaScript
##nested dictionary:
person = {
	'person1': {
		'fname': "Jan",
		'lname': "POgi"
	},
	'person2': {
		'fname': "Neil",
		'lname': "Oneil"
	}
}
print(person['person2']['lname'])
##ForLoop in Python:
for i in List:
	print(i)
##
i = 0
for i in range(10):
	print('{} iteration through the loop.'.format(i))
	i += 1
##WhileLoop in Python:
i = 0
while i < 10:
	print('{} iteration through the loop.'.format(i))
	i += 1
##If/Else Statement
name = "Dagul"
num = 9
if name == "Dagul":
	if num == 9:
		print("He's name is {} and he's number {}".format(name, num))
	else:
		print("He's name is {} and he's number in 1".format(name))
elif name == "Jan":
	print("He's name is {}".format(name))
else:
	print("That's not neither of em.")
##Sample function with simple logic
##def - definition
mySentence = "loves this fast "
carList = ['TypeR','GTR','mazdaspeed3','M4', 'R34']

def carFunction(name):
	lst = []
	for i in carList:
		msg = "{} {} {}".format(name, mySentence, i)
		lst.append(msg)
	return lst

def getName():
	go = True
	while go:
		name = input('What is your name? ')
		if len(name) <= 0:
			print('Please provide a name ')
		elif name == "Bob":
			print('Bob can\'t drive stick shift.')
		else:
			go = False
	lst = carFunction(name)
	for i in lst:
		print(i)
getName()

##Logic Operators:
##AND
##Both conditions are True
num1 = 1
num2 = 5
num1 < num2 and num1 != num2
##OR
##The 'or' operator is used when either operand being compared may evaluate to True. 
##They both do not need to be true just as long as one of them equates to True.
num1 = 1
num2 = 5
num1 < num2 or num1 == num2
##NOT
##This returns as True. The results would have been False if not for the presence of the NOT operator. Confusing huh?!
num1 = 1
num2 = 5
not num1 == num2
##== Double Equal Signs
##Here the integer value for 6 is being compared to the string literal value of '6'. 
##A string is not the same as a number so this would evaluate to False.
6 == '6'
##!= NOT EQUAL TO
##In this example, 6 is not equal to 7 so this statement would evaluate to True
a = 6
b = 7
a != b
##> Greater Than
##Here, 6 is larger than 3 so this evaluates with True
a = 3
b = 6
b > a
##>= Greater Than, Equal To
##For this example, neither is greater but both are still equal, so this would still evaluate to True
a = 2
b = 2
a >= b
##< Less Than
##In this statement, 1 is less than 3 so it would be evaluated as True
a = 1
b = 3
a < b
##<= Less Than, Equal To
##For this statement, neither 'a' nor 'b' have equal value but 12 is less than 40 so this still evaluates to True
a = 12
b = 40
a <= b

##Advance Arithmetic Operations:

## % Modulus
a = 2
b = 11
b  %  a
##11 / 2 = 5 with a remainder of 1
##2 can go into 11, exactly 5 times which is 10
##Now we can take the 11 - 10 to get the remainder of 1
##So this statement would evaluate to a modulus of 1

## ** Exponent
a = 2
b = 4
a ** b
##2 * 2 * 2 * 2
##2 * 2 = 4
##4 * 2 = 8
##8 * 2 = 16
##This would evaluate to 16

