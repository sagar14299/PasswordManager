#PROGRAM TO STORE PASSWORDS

import json
accDict = {}        #used to store master name and password
def sign_in() :
    pass


def create_acc() :
    account = open("Master_pass.json","w+")
    #json_acc = json.load(account)

    
    #asking for uname n pass
    uName = input("Enter username :")
    mPass1 = input("Enter your password : " )

    #checking if pass entered 2 times is correct
    while True :
        mPass2 = input("Re-enter your password : ")
        if mPass1 == mPass2 :
            accDict.update({uName : mPass1})
            break
        else :
            print("Password Mismatch!")
    
    #dumping the dictionary to text file
    
    print("Account created successfully!!")
    sign_in()

    """for i in accDict.items() :
        print(i)"""
    account.close()

#starting point 
print("Do you want to :\n 1. Create a new account \n 2. Sign in with existing account ")
try :
    def start_opt():
        ans = int(input("Choose an option :"))
        if ans == 1 :
            create_acc()
        elif ans == 2 :
            sign_in()
        else:
            print("Invalid Index! Try again.")
            start_opt()
    start_opt()

except ValueError as error :
    print(error)
    start_opt()
