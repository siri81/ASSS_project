import os

def vulnerable_file_read(filepath):
    # Path traversal vulnerability
    with open(filepath, 'r') as f:
        return f.read()

# Example test case
print(vulnerable_file_read("../../etc/passwd"))
