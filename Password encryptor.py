import hashlib

def encrypt_password(password):
  # Encrypt the password using the SHA-256 algorithm
  encrypted_password = hashlib.sha256(password.encode()).hexdigest()
  return encrypted_password

# Test the function
password = "mypassword"
encrypted_password = encrypt_password(password)
print(encrypted_password)