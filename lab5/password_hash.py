import hashlib

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -------- Plaintext Storage --------
print("---- Plaintext Password Storage ----")
plain_password = input("Enter password: ")
stored_plain = plain_password

print("Stored Password (Plaintext):", stored_plain)

# -------- Hashed Storage --------
print("\n---- Hashed Password Storage ----")
password = input("Enter password: ")
stored_hash = hash_password(password)

print("Stored Hash:", stored_hash)

# -------- Login Verification --------
print("\n---- Login ----")
login_password = input("Enter password to login: ")
login_hash = hash_password(login_password)

if login_hash == stored_hash:
    print("Login Successful!")
else:
    print("Login Failed!!")
