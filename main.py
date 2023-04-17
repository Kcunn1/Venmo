user_one = {
    "full_name" : "Rick Grimes",
    "username" : "rick123",
    "password" : "CarlJudith321",
    "account_balance" : 1936,
    "connected_banks" : [("Bank of America", 506), ("Great Union", 680), ("City Bank", 750)]
}
user_two = {
    "full_name" : "Jon Snow",
    "username" : "jsnow300",
    "password" : "dany.789",
    "account_balance" : 850,
    "connected_banks" : [("Great Union", 200) , ("Red Keep Bank", 460), ("Citadel", 190)]
}

# username = input("Please enter your username! ")

# while username != user_one["username"]: 
#     print(f"Entered username is: {username}")
#     username = input("Please try again! ")

# password = input("Please enter your password! ")

# while password != user_one["password"]:
#     password = input("Please try again ")

# print("Verification successful! Welcome!")

# print(f"Your available balance is \n{user_one['account_balance']} ")

# print(f"Your available funds from connected banks are as listed: ")

# for number in range(len(user_one["connected_banks"])):
#     print(f"{user_one['connected_banks'][number][0]}: {user_one['connected_banks'][number][1]}")

print("Beginning user transaction... Please wait")
def transfer_money ():
    while True :
        answer = input(f"Would you like to proceed with transfer to {user_two['full_name']}? y/n ")
        if answer == "n":
             print(f"Transaction cancelled... Your account balance is {user_one['account_balance']}")
             print("Goodbye")
             break
        if answer == "y":
            print(f"Proceeding with transfer to {user_two['full_name']}!")
            amount = input(f"How much would you like to transfer? (whole numbers only)")
            if int(amount) >= user_one["account_balance"]:
                print(f"Insufficient funds.. Your current account balance is {user_one['account_balance']}")
                amount = input(f"How much would you like to transfer?")
            if int(amount) <= user_one["account_balance"]:
                user_one["account_balance"]= user_one["account_balance"]- int(amount)
                user_two["account_balance"]= user_two["account_balance"]+ int(amount)
                print(f"Your remaining balance is \n{user_one['account_balance']}")
            
transfer_money()