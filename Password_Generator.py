import random
def password_gen():

    length = int(input("Enter the Length of password you want"))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = "".join(random.sample(chars, length))
    return password

print (password_gen())  
