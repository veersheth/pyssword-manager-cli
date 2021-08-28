import random
import sqlite3

passwords = []

nums = ['1','2','3','4','5','6','7','8','9','0']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbols = ['@','#','$','%','&','.','-','_']

everyChar = nums + lowercase + uppercase + symbols


mainPassword = "very_secret_password123" # THIS IS THE MAIN PASSWORD TO GET THE PROGRAM WORKING

# GENERATING THE PASSWORD

def make_password():

    password = ""
    for i in range (0,17):
        password = password + random.choice(everyChar)

    return password

# ADDS THE PASSWORD TO THE DATABASE

def add_password(password):
    print("Making a new password")
    print(f"Password is '{password}'")

    if input("Do you want to keep this password? y/n \n") == 'n':
        pass
        
    else:
        password_for = input("What is this password for? \n").lower()
        conn.execute(f"INSERT INTO passwords VALUES('{password_for}', '{password}')")


# RETRIEVING PASSWORDS

def retrieve_password():
    retrieveInput = input("Which password do you want to retrive? \n").lower()
    select_query = """SELECT * from passwords"""
    cursor.execute(select_query)
    records = cursor.fetchall()

    for row in records:
        if row[0] == retrieveInput:
            retrieveOutput = row[1]

    print(f"Password is {retrieveOutput}")
    

    print("")
    print("")


# MAIN LOOP

try: # MAKE THE DATABSE IF IT DOESN'T ALREADY EXIST
    conn = sqlite3.connect("Password_Database.db")
    conn.execute("CREATE TABLE passwords (password_for text, password text)")
    cursor = conn.cursor()
    print("Making your password database \n")

    print("The next time you access the database, a master password will be used to make sure it is you\n")
    print(f"'{mainPassword}' is you password, remember it well\n")

except:
    print("Importing your database \n")
    

tryPassword = input("What is you password? \n")

while tryPassword != mainPassword:
    print("Wrong password try again")
    tryPassword = input("What is you password? \n")

print("\n--- \n\nWelcome, User \n")

while True:

    reason = input("""--- \n
Type:
nw: To make a new password
rt: To retrieve a password
qt: To quit \n
---\n
""")
    
    if reason == "nw":
        add_password(make_password())
        conn.commit()

    if reason == "rt":
        retrieve_password()

    if reason == "qt":
        break