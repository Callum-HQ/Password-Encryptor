import hashlib

def encrypt_password(password):
  encrypted_password = hashlib.sha256(password.encode()).hexdigest()
  return encrypted_password

password = "mypassword"
encrypted_password = encrypt_password(password)
print(encrypted_password)
