# Import the datetime module to get the current date and time
import datetime

# Create an empty list to store the user data
user_data = []

while True:
    # Ask for the user's name, age, gender, and store the current date and time
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    gender = input("Enter Your Gender (M/F): ")
    current_datetime = datetime.datetime.now()

    # Store the user data in a dictionary
    user_dict = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Date and Time": current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    }

    # Add the user data to the list
    user_data.append(user_dict)

    # Ask if the user wants to add another user
    response = input("Do you want to add another user? (y/n): ")
    if response.lower() != "y":
        break

# Print the user data in a table format
print("User Data:")
print("----------")
print("{:<10} {:<5} {:<10} {:<20}".format("Name", "Age", "Gender", "Date and Time"))
print("----------")
for user in user_data:
    print("{:<10} {:<5} {:<10} {:<20}".format(user["Name"], user["Age"], user["Gender"], user["Date and Time"]))
with open('1.txt', 'a') as main1:
    main1.write(str(user_data))
    main1.close()
