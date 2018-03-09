'''
Question:
Given a 2D array A, your task is to convert all rows to columns and columns to rows.

Input: 
First line contains 2 space separated integers, N - total rows, M - total columns. 
Each of the next N lines will contain M space separated integers.

Output: 
Print M lines each containing N space separated integers.

SAMPLE INPUT - 
3 5
13 4 8 14 1
9 6 3 7 21
5 12 17 9 3

SAMPLE OUTPUT
13 9 5
4 6 12
8 3 17
14 7 9
1 21 3

'''

#Solution

#Create List
elements = []
value  = input()
lst = value.split(" ")
row = int(lst[0])
column = int(lst[1])

for i in range(row):
    #Appending list inside elements to create it multidimensional
    elements.append([])
    column_values = input()   
    col_lst = column_values.split(" ")
    for col in range(column):
        elements[i].append(col_lst[col])

# Printing Element in Transpose Order
for col in range(column):
    for i in range(row):
        print (elements[i][col], end=" ")
    print(end="\n")

