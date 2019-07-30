"""

 Created by akiselev on 2019-06-18
 
Neo has a complex matrix script.
The matrix script is a X grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N
(rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.


Note: A 0 score will be awarded for using 'if' conditions in your code.
"""
#!/bin/python3
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

lst = [list(i) for i in zip(*matrix)]
txt = "".join(str(r) for v in lst for r in v)
txt = re.split(r"(?<=\w)[^\w]+(?=\w)", txt)
text = " ".join(str(e) for e in txt)
print(text)