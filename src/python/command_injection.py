import os

def vulnerable_command_injection(user_input):
    # Command injection vulnerability
    os.system(user_input)

# Example test case
vulnerable_command_injection("ls; echo 'Injected Command'")
