# Ask the user for their age and convert it to an integer
age = input("What is your age? ")
age_int = int(age)

# Check various age ranges and provide corresponding messages
if age_int >= 40 and age_int < 64:
    print("You're over the hill.")  # Message for ages between 40 and 63
elif age_int > 100:
    print("Sorry you're dead.")  # Message for ages over 100
elif age_int >= 65 and age_int <= 100:
    print("Enjoy your retirement!")  # Message for ages between 65 and 100
elif age_int < 13:
    print("You qualify for the kiddie discount.")  # Message for ages under 13
elif age_int == 21:
    print("Congrats on your 21st!")  # Message for age 21
else:
    print("Age is but a number.")  # Default message for all other ages
