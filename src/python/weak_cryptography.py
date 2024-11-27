from Crypto.Cipher import DES

def weak_cryptography(data):
    # Weak cryptography: DES encryption (insecure)
    key = b"12345678"  # 8-byte key
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data.ljust(16))  # Pad to match block size

# Example test case
print(weak_cryptography(b"InsecureData"))
