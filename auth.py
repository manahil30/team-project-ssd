def login(username, password):
    if username == "admin" and password == "secure123":
        return True
    return False

def logout():
    return "User logged out"
