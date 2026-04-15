import hashlib
import os

user_db = {}

def hash_password(password: str, salt: bytes = None):
    """Hashes a password with a salt using PBKDF2."""
    if salt is None:
        salt = os.urandom(16) # Generate a secure random salt
    
    # 100,000 iterations of SHA-256
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key

def register_user(username, password):
    """Registers a new user by securely hashing their password."""
    if username in user_db:
        print(f"[-] Registration failed: User '{username}' already exists.")
        return False
        
    salt, key = hash_password(password)
    user_db[username] = {
        'salt': salt,
        'key': key
    }
    print(f"[+] User '{username}' registered successfully.")
    return True

def authenticate_user(username, password):
    """Authenticates a user by verifying the provided password against the stored hash."""
    if username not in user_db:
        print(f"[-] Authentication failed: User '{username}' not found.")
        return False
        
    stored_salt = user_db[username]['salt']
    stored_key = user_db[username]['key']
    
    # Hash the provided password with the stored salt
    _, new_key = hash_password(password, stored_salt)
    
    # Compare the newly generated hash with the stored hash
    if new_key == stored_key:
        print(f"[+] Authentication successful! Welcome, {username}.")
        return True
    else:
        print("[-] Authentication failed: Incorrect password.")
        return False

if __name__ == "__main__":
    print("--- Testing Authentication ---")
    register_user("dilpreet", "CORRECTPASS")
    
    # Attempting to login with correct password
    authenticate_user("dilpreet", "CORRECTPASS")
    
    # Attempting to login with incorrect password
    authenticate_user("dilpreet", "WrongPassword")
