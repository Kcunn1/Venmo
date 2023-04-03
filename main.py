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

username = input("Please enter your username! ")

while username != user_one["username"]: 
    print(f"Entered username is: {username}")
    username = input("Please try again! ")

password = input("Please enter your password! ")

while password != user_one["password"]:
    password = input("Please try again ")

print("Verification successful! Welcome!")

print("Your available balance is: ")
print(user_one["account_balance"])

print("Your available funds from connected accounts are:")
