"""

 Created by akiselev on 2019-06-13

We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])

TASK
You are given a set
and number of other sets. These number of sets have to perform some specific mutation operations on set

.

Your task is to execute those operations and print the sum of elements from set
.



 
The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

The syntax of getattr() method is:

getattr(object, name[, default])

The above syntax is equivalent to:

object.name

better option than eval!
"""

_, A = input(), set(input().split())
for _ in range(int(input())):
    op, _ = input().split()
    B = set(input().split())
    #eval("A.{}(B)".format(op))
    getattr(A, op)(B)
print (sum(map(int,A)))