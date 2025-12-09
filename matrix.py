print("Enter matrix rows (press Enter on empty line to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)


mat = [[int(x) for x in line.split()] for line in lines]


sum_rows = [sum(row) for row in mat]


sum_cols = [sum(col) for col in zip(*mat)]


num_rows = len(mat)
num_cols = len(mat[0])


print("Row sums:")
for i in range(num_rows):
    print(f"Row {i+1}: {sum_rows[i]}")

print("Column sums:")
for i in range(num_cols):
    print(f"Column {i+1}: {sum_cols[i]}")
