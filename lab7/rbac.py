ROLES_PERMISSIONS = {
    'admin': ['create_user', 'delete_user', 'read_data', 'write_data'],
    'manager': ['read_data', 'write_data'],
    'guest': ['read_data']
}

USER_ROLES = {
    'amar': 'admin',
    'akbar': 'manager',
    'anthony': 'guest'
}

def get_user_permissions(username):
    """Retrieves the list of permissions for a given user based on their role."""
    role = USER_ROLES.get(username)
    if role:
        return ROLES_PERMISSIONS.get(role, [])
    return []

def check_access(username, action):
    """Checks if a user has the authorization to perform a specific action."""
    permissions = get_user_permissions(username)
    
    if action in permissions:
        print(f"[+] SUCCESS: '{username}' is AUTHORIZED to '{action}'.")
        return True
    else:
        print(f"[-] DENIED: '{username}' is NOT AUTHORIZED to '{action}'.")
        return False

# --- Testing Part B ---
if __name__ == "__main__":
    print("\n--- Testing Role-Based Access Control ---")
    
    # amar is an admin, she should be able to delete users
    check_access("amar", "delete_user")
    
    # akbar is a manager, he can write data but cannot delete users
    check_access("akbar", "write_data")
    check_access("akbar", "delete_user")
    
    # anthony is a guest, he can only read data
    check_access("anthony", "read_data")
    check_access("anthony", "write_data")
    
    # Unknown user
    check_access("dilpreet", "read_data")
