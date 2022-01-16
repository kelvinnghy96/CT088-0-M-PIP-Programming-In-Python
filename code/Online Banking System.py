#Use Admin ID and Password to create first customer account
#Admin Id : kv
#Admin Password : 123

#Define function
#view(), to view transaction based on username input and return the sum of transaction
def view(a,b):
    tlist = []
    sum = 0
    #Sum up transaction in text file based on username and category(deposit/withdrawal)
    file = open("../data/"+a+" "+b+".txt","r")
    for transaction in file:
        tlist.append(float(transaction.strip()))
        sum = sum + float(transaction)
    file.close()
    return sum

#record(), to read the transaction, get input from user and store it in the text file. Return the sum of transaction with new input added.                
def record(a,b):
    tlist = []
    sum = 0
    #Sum up transaction in text file based on username and category(deposit/withdrawal)
    file = open("../data/"+a+" "+b+".txt","r")    
    for transaction in file:
        tlist.append(float(transaction.strip()))
        sum = sum + float(transaction)
    file.close()

    #Error handling and prompt user to enter number only
    try:
        amt = float(input("Enter an amount for "+b+": "))
    except Exception as error:
        print("\nError!.\nPlease enter number only.\n")
        quit()

    #To ensure user input valid withdrawal amount. User cant input amount exceed it account balance.
    if amt > 0:
        #If category is withdrawal, read withdrawal list
        if b == "withdrawal" and amt <= (view(username,"deposit") - view(username,"withdrawal")):
            sum = sum + amt
            tlist.append(amt)
            file = open("../data/"+a+" "+b+".txt","w")
            for t in tlist:
                file.write(str(t)+"\n")
            file.close()
        #If category is deposit, read deposit list
        elif b == "deposit":
            sum = sum + amt
            tlist.append(amt)
            file = open("../data/"+a+" "+b+".txt","w")
            for t in tlist:
                file.write(str(t)+"\n")
            file.close()
    else:
        print("Please enter valid value.")
    return amt,sum


#Starting interface for the system
print("----------------------------------"
      "\nWelcome to Online Banking System."
      "\nPlease select your role."
      "\n----------------------------------")


#Reset role counter
role = ""

#Get role input from user
role = str(input("\n ----------------------------"
          "\n| Enter 1 for Admin role.    |"
          "\n| Enter 2 for Customer role. |"
          "\n| Enter q to quit.           |"
          "\n ----------------------------\n")).strip().lower()

#Looping for login
start = 0
while start != 1:

    #Reset all the counters
    login_counter = 0
    wrong_counter = 0

    #Login
    #Get username and password input from user if they selected their role
    if role == "1" or role == "2":
        username = str(input("\nPlease enter your username: ")).strip().lower() #Ensure all the input from user will remove trailing space and in lowercase
        password = str(input("Please enter your password: ")).strip().lower() #Ensure all the input from user will remove trailing space and in lowercase
        user_pass = username+","+password #Concat username and password into "username,password" format

        #To ensure user did enter something in the username and password
        if len(username)==0 or len(password)==0:
            print("You must enter both username and password.")
        else:
            #Admin Login Check
            #To check whether admin username and password is correct
            if role == "1":
                afile = open("../data/admin list.txt","r")
                for admin in afile:
                    admin = admin.strip()
                    if user_pass == admin:
                        print("Login Successful")
                        login_counter = 1
                        start = 1
                afile.close()

                #To check whether both username and password is wrong
                if login_counter != 1:
                    afile = open("../data/admin list.txt","r")
                    for admin in afile:
                        admin = admin.strip()
                        if admin.startswith(username+","):
                            print("Wrong Password. Please login again.\n")
                            wrong_counter = 1              
                    afile.close()
                    
                    #If both username and password is wrong, account not exist and request user to contact bank
                    if login_counter != 1 and wrong_counter!=1:
                        print("Account not exist. Please contact bank for account creation.\n")
                        
            #Customer Login Check
            #To check whether admin username and password is correct
            elif role == "2":
                cfile = open("../data/customer list.txt","r")
                for customer in cfile:
                     customer = customer.strip()
                     if user_pass == customer:
                        print("Login Successful")
                        login_counter = 2
                        start = 1
                cfile.close()
                
                #To check whether both username and password is wrong
                if login_counter != 2:
                    cfile = open("../data/customer list.txt","r")
                    for customer in cfile:
                        customer = customer.strip()
                        if customer.startswith(username+","):
                            print("Wrong Password. Please login again.\n")
                            wrong_counter = 2     
                    cfile.close()
                    
                    #If both username and password is wrong, account not exist and request user to contact bank
                    if login_counter != 2 and wrong_counter!=2:
                        print("Account not exist. Please contact bank for account creation.\n")
                 

#Looping for task and service
end = ""
while end != "q":

    #Reset all the counters
    task = ""
    service = ""
    create = 0

#Task selection
    #Admin task selection
    #User will only reach this page when user choose for admin role
    #Request user to select one of the task or quit
    if role == "1" and login_counter == 1:
        task = str(input("\n --------------------------------------------------------"
          "\n| Enter 1 to create new customer's profile.              |"
          "\n| Enter 2 to view and search customer's profile.         |"
          "\n| Enter 3 to view all transactions of specific customer. |"               
          "\n| Enter q to quit.                                       |"
          "\n --------------------------------------------------------\n")).strip().lower()#Ensure all the input from user will remove trailing space and in lowercase

    #Customer service selection
    #User will only reach this page when user choose for customer role
    #Request user to select one of the service or quit
    if role == "2" and login_counter == 2:
        service = str(input("\n -------------------------------"
          "\n| Enter 1 to Deposit.           |"
          "\n| Enter 2 to Withdrawal.        |"
          "\n| Enter 3 to view transactions. |"               
          "\n| Enter q to quit.              |"
          "\n -------------------------------\n")).strip().lower()#Ensure all the input from user will remove trailing space and in lowercase

    #End WHILE loop if user enter "q"
    if role == "q" or task == "q" or service == "q":
        end = "q"

#Admin tasks
    #Admin task 1 - Create new customer's profile
    if task == "1":
        new_username = str(input("\nPlease enter a new username: ")).strip().lower()
        new_password = str(input("Please enter a new password: ")).strip().lower()
        #Check whether the new username and password input is in the customer list
        cfile = open("../data/customer list.txt","r")
        for customer in cfile:
            customer = customer.strip()
            if customer.startswith(new_username+","):
                print("Account already exist.")
                create = 1
        cfile.close()

        #If account not exist, proceed with profile and account creation
        if create != 1:
            print("\nPlease enter the profile correctly."
                  "\nYou CANT change it after the account is created")
            profile_name = str(input("\nEnter customer's name: ")).strip()
            profile_age = int(input("Enter customer's age: "))
            profile_gender = str(input("Enter customer's gender: ")).strip()
            profile_contact = str(input("Enter customer's phone number: ")).strip()
            print("\nProfile created.")
            #Create individual text file to store for each customer's profile
            pfile = open("../data/"+new_username+" profile.txt","w")
            pfile.write("Name\t: "+profile_name+
                        "\nAge\t: "+str(profile_age)+
                        "\nGender\t: "+profile_gender+
                        "\nContact\t: "+str(profile_contact))
            pfile.close()
            #Write new username and password into customer list and username list
            cfile = open("../data/customer list.txt","a")
            cfile.write("\n"+new_username+","+new_password)
            print("Account created.")
            cfile.close()
            ufile = open("../data/username list.txt","a")
            ufile.write("\n"+new_username)
            ufile.close()
            #Open a deposit and withdrawal text file for new user to store their transaction details
            dfile = open("../data/"+new_username+" deposit.txt","w")
            dfile.close()
            wfile = open("../data/"+new_username+" withdrawal.txt","w")
            wfile.close()


        
    #Admin task 2 - View and search customer's profile
    #Show all the username in username list to let user choose which username to search
    if task == "2":
        ufile = open("../data/username list.txt","r")
        print("\nUsername List"
              "\n-------------")
        for username in ufile:
            username = username.strip().lower()
            print(username)
            
        #Search for respective profile text file and display to user
        psearch = str(input("\nEnter username to view customer's profile: ")).strip().lower()
        pfile = open("../data/"+psearch+" profile.txt","r")
        for profile in pfile:
            profile = profile.strip()
            print(profile)
        
    #Admin task 3 - View all transactions of specific customer
    #Show all the username in username list to let user choose which username to search
    if task == "3":
        ufile = open("../data/username list.txt","r")
        print("\nUsername List"
              "\n-------------")
        for username in ufile:
            username = username.strip().lower()
            print(username)

        #Search for respective user transaction in transaction list and display to user
        psearch = str(input("\nEnter username to view customer's transaction: ")).strip().lower()
        tfile = open("../data/transaction list.txt","r")
        print("\nCustomer's Transaction"
              "\n----------------------")
        for transaction in tfile:
            transaction = transaction.strip()
            if(transaction.startswith(psearch+",")):
                print(transaction)
        tfile.close()

#Customer Services
    #Customer service 1 - Deposit
    if service == "1":
        #Check for account balance, deposit - withdrawal
        balance = view(username,"deposit") - view(username,"withdrawal")
        print("Your account balance is",balance)
        #Check valid and record the deposit transaction into deposit list using record()
        deposit , deposit_balance = record(username,"deposit")
        #Sum up deposit entered for new balance
        new_balance = deposit_balance - view(username,"withdrawal")
        if deposit > 0:
            #Write the transaction in transaction list if deposit > 0
            tfile = open("../data/transaction list.txt","a")
            tfile.write("\n"+str(username)+",deposit,"+str(deposit))
            tfile.close()
            print("You have deposit",deposit,"and your new balance is",new_balance)

    #Customer service 2 - Withdrawal
    if service == "2":
        #Check for account balance, deposit - withdrawal
        balance = view(username,"deposit") - view(username,"withdrawal")
        #To ensure user account balance is sufficient to withdraw
        if balance > 0:
            print("Your account balance is "+str(balance)+"."
                  "\nYou can withdraw "+str(balance)+" from your account.")
            #Check valid and record the withdrawal transaction into withdrawal list using record()
            withdrawal , withdrawal_balance = record(username,"withdrawal")
            #To ensure withdrawal input > 0
            if withdrawal > 0:
                if withdrawal <= balance:
                    #Sum up withdrawal entered for new balance
                    new_balance = view(username,"deposit") - withdrawal_balance
                    #Write the transaction in transaction list
                    tfile = open("../data/transaction list.txt","a")
                    tfile.write("\n"+str(username)+",withdrawal,"+str(withdrawal))
                    tfile.close()
                    print("You have withdraw",withdrawal,"and your new balance is",new_balance)
                else:
                    print("\nYour account balance is not sufficient."
                     "\nYou can only withdraw "+str(balance)+" from your account.") 
        else:
            print("Your account balance is not sufficient.")

    #Customer service 3 - View Transaction
    if service == "3":
        #Search for user transaction in transaction list and display to user
        tfile = open("../data/transaction list.txt","r")
        print("\nMy Transactions"
              "\n---------------")
        for transaction in tfile:
            transaction = transaction.strip()
            if(transaction.startswith(username+",")):
                print(transaction)
        tfile.close()











    

