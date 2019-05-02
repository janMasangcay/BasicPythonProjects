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
##ForLoop in Python:
for i in List:
	print(i)
##
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
##
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