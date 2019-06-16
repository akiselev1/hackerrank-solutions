"""

 Created by akiselev on 2019-06-13
 
 Task

The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English,
some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other
set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number
of students who have subscribed to at least one newspaper.

union : A | B
intersection : A & B
difference : A - B
"""

_, Eng = input(), set(input().split())
_, Fr = input(), set(input().split())
print(len(Eng.union(Fr)))
print(len(Eng.intersection(Fr)))
print(len(Eng.difference(Fr)))