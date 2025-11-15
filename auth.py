import bcrypt
import os

# -----------------------
# Hashing Function
# -----------------------
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')


# -----------------------
# Verify Password
# -----------------------
def verify_password(plain_text_password, hashed_password):
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


# -----------------------
# Register User
# -----------------------
def register_user(username, password):
    """Register a new user by hashing password & saving to file."""
    hashed_password = hash_password(password)

    with open("users.txt", "a") as f:
        f.write(f"{username},{hashed_password}\n")

    print(f"User '{username}' registered successfully!")


# -----------------------
# Test Hashing & Verifying
# -----------------------
password = input("Enter password: ")
hashed = hash_password(password)
print("Hashed:", hashed)

check = input("Re-enter password to verify: ")

if verify_password(check, hashed):
    print("Password match!")
else:
    print("Password does not match.")
