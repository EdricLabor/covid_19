age = input("Are you a cigarette addict older than 75 years old?, Yes or No :")
chronic = input("Do you have a severe chronic disease?, Yes or No :")
immune = input("Is your immune system too weak?, Yes or No :")

if age.upper() == "YES":
    age = True
else:
    age = False

if chronic.upper() == "YES":
    chronic = True
else:
    chronic = False

if immune.upper() == "YES":
    immune = True
else:
    immune = False

if age or chronic or immune:
    print("You are in risky group")
else:
    print("You are not in risky group")