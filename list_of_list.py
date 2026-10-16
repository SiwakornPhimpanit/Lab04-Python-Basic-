row1 =[]
row1.append(1)
row1.append(2)  
row1.append(3)


print(row1)  # Output: [1, 2, 3]

row2 = []
row2.append(4)
row2.append(5)
row2.append(6)

row3 = []
row3.append(7)
row3.append(8)
row3.append(9)

table = []
table.append(row1)
table.append(row2)
table.append(row3)
print(table)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_table(table):
    for row in table:
        for item in row:
            print(item, end=' ')
        print()  # New line after each row

print("Table:")
print_table(table)
