import hashlib

def generate_hash(password):   
  m = hashlib.sha256(password.encode())
  return m.hexdigest()

def verify_password(password,password_hash):
  if generate_hash(password) == password_hash:
    return True
  return False

password = 'python'
password_hash = generate_hash(password)
print(verify_password('piton',password_hash)) # coba dengan password salah
print(verify_password('python',password_hash)) # coba dengan password yang benar