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

def decrypt_matrix(matrix):
    alpha_chars = [''] * len(matrix[0])
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col].isalpha():
                alpha_chars[col] += matrix[row][col]

    decoded_message = ' '.join(alpha_chars)
    
    return decoded_message

decoded_message = decrypt_matrix(matrix)
print(decoded_message)