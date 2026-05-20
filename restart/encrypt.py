def getMessage():
    string = input("Enter your message: ")
    return string


def getSecretKey():
    key = input("Enter your key: ")
    return key


def encrypt(message):
    encrypted = ""
    for char in message:
        encrypted += chr(ord(char) + 1)
    return encrypted


def decrypt(encrypted):
    decrypted = ""
    for char in encrypted:
        decrypted += chr(ord(char) - 1)
    return decrypted
