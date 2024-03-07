#Imani Hollie 03/06/2024
#Ch. 8 Arrays

#Lists
#In Python, you create lists instead of arrays, which is similar to, but more
#capable than the traditonal array. A list is a an object that contains multiple
#data items. Each item stored in a list is called an element. Objects enclosed in
#brackets ([]) and separated by commas (,) are the values of the elements.
#Ex1. Here is a statement that creates a list of integers (int):
#even_numbs = [2, 4, 6, 8, 10]
#Ex2. Here is a statement that creates a list of strings:
#names = ['Molly', 'Steven', 'Will', 'Alicia', 'Adriana']
#You can use the 'print' function to display an entire list, as shown here:
#Ex3. numbs = [1, 2, 3, 4, 5]
#	  print(numbs)

#List Elements and Subscripts in Python
#Each element can be accesses with a subscript; The first element's subscript is
#0, then 1, etc. The last element's subscript is the array size - 1.
#Ex4. The following code creates a list named numbs, with 3 elements that are all
#set to 0. It then assigns different values to each element. The subscripts for
#the elements are 0, 1, and 2.
#numbs = [0, 0, 0]
#numbs[0] = 10
#numbs[0] = 20
#numbs[0] = 30

#Using 'len' function with Lists in Python
#An error will occur if you use an invalid index with a list. You can use the
#'len' function to get the length of a list in Python.
#Ex5. When a list is passed as an argument, the 'len' function returns the
#number of elements in the list.
#my_list = [10, 20, 30, 40, 50]
#index = 0
#while index < len(my_list):
#	print(my_list[index])
#	index += 1

#Iterating Over a List with the 'for' Loop in Python
#In Python, you can easily iterate over the contents of a list with the 'for'
#loop by assigning a named variable (n) a copy of the first value in the list,
#and then executing the statements in the block, and repeating until the last
#value in the list. Any chnages made to the n variable do not affect the list.
#Ex6. numbs = [1, 2, 3, 4, 5]
#	  for n in numbs:
#	  	  print(n)

#Passing List as an Argument to a Function in Python


#2-D Lists in Python


#Rows and Columns