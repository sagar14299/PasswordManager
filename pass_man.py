#PROGRAM TO STORE PASSWORDS
import os, json

def managing(userName) :
    print("Hello "+userName+". Do you want to :\n 1. Store passwords \n 2. See passwords ")
    try:
        ans = int(input("Choose an option :"))
        if ans == 1 :
            #storing info
            with open("master_pass.json","r+") as fp :
                acc_name = input("Enter the name of service you want to store info for: ")
                uName = input("Enter email or username: ")
                password = input("Enter password: ")
                acc_info = {uName : password}
                #again loading n dumping
                data = json.load(fp)
                data[userName] = data.get(userName,[]) + [{acc_name : acc_info}]
                print(data.values())
                fp.seek(0)
                json.dump(data, fp, indent=4)
                print("Data Saved!!\n")
            managing(userName)
        
        elif ans == 2 :
            print("\nYou have following information stored:")
            with open("master_pass.json","r+") as fp :
                data = json.load(fp)
                items = data.get(userName)
                #getting dicts stored in list on master username
                dic = {}
                for i in items[1:] :
                    dic.update(i)
                print(list(dic.keys()))
                #asking which account to show info for :
                key = input("Give the name of info you want to see: ")
                info = dic.get(key,None)
                try :
                    print("UserName: "+str(list(info.keys()))+"\nPassword: "+str(list(info.values())))
                except :
                    print(None)
            managing(userName)
        
        else:
            print("Invalid Index! Try again.")
            managing(userName)

    except ValueError as error :
        print(error)
        managing(userName)


def sign_in() :
    with open("master_pass.json","r") as fp :
        data = json.load(fp)
        while True :
            userName = input("Enter username: ")
            if userName in data.keys() :
                break
            else :
                print("No such username")
        while True :
            mPass = input("Enter password: ")
            if any(mPass in val for val in data.values() ) :    #returns true if there is any mpass in value i.e list and val is dict value which is looped through and returns true if exist
                break
            else :
                print("Incorrect Password")
        managing(userName)

def create_acc() :
    fp = open("master_pass.json","a+")
    if os.stat("master_pass.json").st_size ==0 :
        dummy = {"Username" : "Password"}
        json.dump(dummy, fp, indent=4)
    fp.close()
    accDict = {}        #used to store master name and pass
    #asking for uname n pass
    uName = input("Enter username :")
    mPass1 = input("Enter your password : " )

    #checking if pass entered 2 times is correct n dumping it to json
    while True :
        mPass2 = input("Re-enter your password : ")
        if mPass1 == mPass2 :
            accDict.update({uName : [mPass1]})
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
