import sys

print("Enter a string to be converted as first argument and the choice: lower or upper or title to be converted to as the second argument.")

usr_data = sys.argv[1]
usr_choice = sys.argv[2]

if usr_choice == "lower":
    print(usr_data.lower())
elif usr_choice == "upper":
    print(usr_data.upper())
elif usr_choice == "title":
    print(usr_data.title())
else:
    print("You did not choose th right choice. GoodBye...!!!")
