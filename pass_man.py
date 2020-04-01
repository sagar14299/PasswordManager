#PROGRAM TO STORE PASSWORDS
import os
import json

fp = open("master_pass.json","a+")
if os.stat("master_pass.json").st_size ==0 :
    dummy = {"Username" : "Password"}
    json.dump(dummy, fp, indent=4)
fp.close()

def sign_in() :
    pass

def create_acc() :

    accDict = {}        #used to store master name and password
    #asking for uname n pass
    uName = input("Enter username :")
    mPass1 = input("Enter your password : " )

    #checking if pass entered 2 times is correct n dumping it to json
    while True :
        mPass2 = input("Re-enter your password : ")
        if mPass1 == mPass2 :
            accDict.update({uName : mPass1})
            with open("master_pass.json","r+") as fp :
                data = json.load(fp)
                data.update(accDict)
                fp.seek(0)
                json.dump(data, fp, indent=4)
                print("Account Created!!")
            break
        else :
            print("Password Mismatch!")
    
    sign_in()

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
