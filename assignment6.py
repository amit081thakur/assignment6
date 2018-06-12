Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
>>> #Q.1- Take 10 integers from user and print it on screen. 
>>> for x in range(10):
	print("\n enter the name:")
	name = str(input())
	print("\nthe name is:",name)

	

 enter the name:
amit

the name is: amit

 enter the name:
th

the name is: th

 enter the name:
uk

the name is: uk

 enter the name:
fk

the name is: fk

 enter the name:
rj

the name is: rj

 enter the name:
hl

the name is: hl

 enter the name:
fk

the name is: fk

 enter the name:
fk

the name is: fk

 enter the name:
du

the name is: du

 enter the name:
rh

the name is: rh
>>>
>>>
>>>
>>> #Q.2- Write an infinite loop.An infinite
>>> #loop never ends. Condition is always true.
>>>
>>>>>> while(count>9):
		   print("amit")

		   
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit
amit


>>> #Q.3- Create a list of integer elements by user input.
>>> #Make a new list which will store square of elements of previous list. 
>>>
>>> list=[]
>>> for i in range(5):
	list.append(input('enter number'))

enter number78
enter number90
enter number90
enter number56
enter number34
>>> list
['78', '90', '90', '56', '34']
>>> square(list)
['7878', '9090', '9090', '5656', '3434']
>>>
>>>
>>>
>>> #Q.4- From a list containing ints, strings and
>>> #floats, make three lists to store them separately 
>>> 
>>> list=[1,2,3,4,"abc","acd",4.6,8.9]
>>> integ=[]
>>> strin=[]
>>> floatt=[]
>>> for i in range(len(list)):
	if type(list[i])==int:
		integ.append(list[i])
	if type(list[i])==str:
		strin.append(list[i])
	if type(list[i])==float:
		floatt.append(list[i])

		
>>> print(integ)
[1, 2, 3, 4]
>>> print(strin)
['abc', 'acd']
>>> print(float)
<class 'float'>
>>> print(floatt)
[4.6, 8.9]
>>> 
>>>
>>>
>>>
>>> #Q.5- Using range(1,101), make a list containing even and odd numbers. 
>>>
>>> list=[]
>>> list1=[]
>>> list2=[]
>>> for x in range(1,101):
	list.append(x)

	
>>>  for i in range(len(list)):
	
SyntaxError: unexpected indent
>>> for i in range(len(list)):
	if i%2==0:
		list1.append(i)
	else:
		list2.append(i)

		
>>> print(list1)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> print(list2)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>>
>>>
>>>
>>>
>>> #Q.6- Print the  pattern
>>>
>>> n=0
>>> for x in range(0,5):
	print('*'*n)
	n=n+1

	

*
**
***
****
>>>
>>>
>>>
>>> #.7- Create a user defined dictionary and
>>> #get keys corresponding to the value using for loop.
>>>
>>>
>>> list=[]
>>> for i in range(0,11):
	list.append(i)

	
>>> x = int(input("number selected:"))
number selected:3
>>> list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for i in range(len(list)):
	if i==x:
		list.remove(i)

	
>>> list
[0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>>
>>>
>>> #Q.8- Take inputs from user to make a list. Again take one input from user
>>> #and search it in the list and delete that element, if found
>>> #.Iterate over list using for loop.
>>>
>>>
>>>  dict={'amit':34,'dinesh':67,'arjun':45}
>>>
>>>
>>> for key in dict:
	print(key,"=>",dict[key])

amit => 34
dinesh => 67
arjun => 45
>>> 
