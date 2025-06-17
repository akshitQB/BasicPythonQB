import hashlib
message = "Hello, World!"
hashed = hashlib.blake2b(message.encode()).hexdigest()
print(hashed)