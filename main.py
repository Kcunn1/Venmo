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

username = "rick123"
password = "CarlJudith321"

while password != user_one["password"] or username != user_one["username"]: 
    
