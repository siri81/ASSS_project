from http.cookies import SimpleCookie

def insecure_cookie():
    # Missing secure cookie flag
    cookie = SimpleCookie()
    cookie["session"] = "abc123"
    # Insecure: no Secure or HttpOnly flags
    print(cookie.output())

# Example test case
insecure_cookie()
