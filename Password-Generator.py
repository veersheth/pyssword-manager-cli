import random
passwords = []

nums = ['1','2','3','4','5','6','7','8','9','0']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['@','#','$','%','&','.','-','_']

everyChar = nums + lowercase + uppercase + symbols

def makePassword():

    password = ""

    for i in range (0,17):
        password = password + random.choice(everyChar)

    return password

while True:
    formedPassword = makePassword()
    print(f"Your password is '{formedPassword}'")
    savePoint = input("What is this password for? ")
    passwords.append({savePoint: formedPassword])
    if input("Continue? ") == "No":
        break




print(passwords)

