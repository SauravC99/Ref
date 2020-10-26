################# Data Structures #########################

#---------------------------------List Array
list = [1, 2, 3, 4, 5, 6]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

#add to end
list.append(3)
thislist.append("lemon")

#insert (inserts before the 2nd index)
#(inserts at begining, or before 0th index)
list.insert(2, 55)
thislist.insert(0, "Bongo")

#remove the value
list.remove(55)
thislist.remove("Bongo")

#pop and return the value at i, if it is blank, remove last item
list.pop(3)

#remove all items
list.clear()

#index return 0 baseed index of first value equal to x
list.index(2)
thislist.index("banana", 4) # Find next banana starting a position 4

#return the number of times x is in list
thislist.count("apple")

#sort in place
list.sort()

#reverse the elements of the list
thislist.reverse()

#return a shallow copy
list.copy()

#----------------------------------------------Stacks
#Stack is last in first out
#to add to the top of stack use append()
#to retrueve and remove from top of stack use pop()

"""
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
"""

#------------------------------------------Queue
#Queue is first in first out
#lists are not efficient for this bc insert and
#pop from begining are slow (have to shift other elements by 1)
#use collections.deque

"""
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
"""

#------------------------Tuples
#immutable
"""
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])


>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)

The statement t = 12345, 54321, 'hello!' is an example of 
tuple packing: the values 12345, 54321 and 'hello!' are 
packed together in a tuple. The reverse operation is also possible:

>>> x, y, z = t
"""


"""
DFS
BFS
Binary Tree
Binary Search


Linked List
Dictionary

Tuples

Bubble Sort
Selection Sort
Merge Sort
Counting Sort
MSS - O(n) version

GCC Sort
Sets

"""