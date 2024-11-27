import hashlib

def weak_hashing(data):
    # Weak hashing: MD5 (insecure)
    return hashlib.md5(data.encode()).hexdigest()

# Example test case
print(weak_hashing("password123"))
