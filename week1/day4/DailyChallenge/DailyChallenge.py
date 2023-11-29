matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

mat = ''.join(matrix)

num_of_columns = len(matrix[0])
def calc_index(row, col):
    return col * num_of_columns + row
alpha_chars = []
for row in range(num_of_columns):
    for column in range(len(matrix)):
        index = calc_index(row, column)
        if mat[index].isalpha() or mat[index] == ' ':
            alpha_chars.append(mat[index])
print(''.join(alpha_chars))
