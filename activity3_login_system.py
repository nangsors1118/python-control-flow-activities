correct_username = "admin"
correct_password = "python123"

while True:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")  # Correct credentials
        break
    else:
        print("Try again!")         # Wrong credentials
