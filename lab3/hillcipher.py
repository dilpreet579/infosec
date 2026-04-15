import numpy as np

def mod_inverse(a, m):
    # Returns x such that (a * x) % m == 1
    try:
        return pow(int(a), -1, m)
    except ValueError:
        raise ValueError(f"Determinant {a} has no inverse mod {m}. Key is invalid.")

# Find Inverse Matrix Mod 26 (Specific for 2x2)
# def find_inverse_matrix(matrix):
#     det = int(np.round(np.linalg.det(matrix)))
#     det_inv = mod_inverse(det, 26)

#     a, b = matrix[0, 0], matrix[0, 1]
#     c, d = matrix[1, 0], matrix[1, 1]

#     adjugate = np.array([
#         [d, -b],
#         [-c, a]
#     ])

#     # Inverse = (det_inv * adjugate) % 26
#     inverse_matrix = (det_inv * adjugate) % 26
#     return inverse_matrix.astype(int)

def find_inverse_matrix(matrix):
    n = len(matrix)
    det = int(np.round(np.linalg.det(matrix)))  # Calculate Determinant
    det_inv = mod_inverse(det % 26, 26)         # Modular Inverse of Det

    # Calculate Adjugate Matrix using Cofactors
    adjugate = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            # Create minor matrix by removing row i and column j
            minor = np.delete(np.delete(matrix, i, 0), j, 1)
            
            # Determinant of minor
            minor_det = int(np.round(np.linalg.det(minor)))
            
            # Cofactor = (-1)^(i+j) * minor_det
            cofactor = ((-1) ** (i + j)) * minor_det
            
            # Adjugate[j][i] is the transpose of Cofactor[i][j]
            adjugate[j, i] = cofactor

    # Inverse = (det_inv * adjugate) % 26
    return (det_inv * adjugate) % 26

def hill_encrypt(message, key_matrix):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_to_num = {c: i for i, c in enumerate(chars)}
    num_to_char = {i: c for i, c in enumerate(chars)}
    
    message = message.replace(" ", "").upper()
    n = len(key_matrix)
    
    # Padding
    while len(message) % n != 0:
        message += 'X'
        
    encrypted_text = ""
    
    for i in range(0, len(message), n):
        block = [char_to_num[char] for char in message[i:i+n]]
        block_vector = np.array(block)
        result_vector = np.dot(key_matrix, block_vector) % 26
        encrypted_text += "".join([num_to_char[num] for num in result_vector])
        
    return encrypted_text

def hill_decrypt(ciphertext, key_matrix):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_to_num = {c: i for i, c in enumerate(chars)}
    num_to_char = {i: c for i, c in enumerate(chars)}
    
    n = len(key_matrix)
    
    try:
        inverse_key = find_inverse_matrix(key_matrix)
    except ValueError as e:
        return str(e)

    decrypted_text = ""
    
    for i in range(0, len(ciphertext), n):
        block = [char_to_num[char] for char in ciphertext[i:i+n]]
        block_vector = np.array(block)
        
        result_vector = np.dot(inverse_key, block_vector) % 26
        decrypted_text += "".join([num_to_char[num] for num in result_vector])
        
    return decrypted_text

# Valid Key Matrix (should be coprime to 26)
# key = np.array([[5, 8], 
#                 [17, 3]])

# 3x3 Key Matrix
key = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

plaintext = "HELLO"

ciphertext = hill_encrypt(plaintext, key)
print(f"Original Plaintext: {plaintext}")
print(f"Key Matrix:\n{key}")
print(f"Ciphertext:         {ciphertext}")

decrypted_msg = hill_decrypt(ciphertext, key)
print(f"Decrypted Text:     {decrypted_msg}")

if plaintext == decrypted_msg.replace('X', ''):
    print("\n[SUCCESS] Decryption verified successfully!")
else:
    print("\n[FAIL] Something went wrong.")
