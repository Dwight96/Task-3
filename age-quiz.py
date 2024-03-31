age = (input("What is your age? ")) 
age_int = int(age)
if age_int >= 40 and age_int < 64:
    print("You're over the hill.") 
elif age_int > 100: 
    print("Sorry you're dead.") 
elif age_int >= 65 and age_int <= 100:
    print("Enjoy your retirement!")
elif age_int < 13: 
    print("You qualify for the kiddie discount.")
elif age_int == 21:
    print("Congrats on your 21st!")  
else:
    print("Age is but a number.")
