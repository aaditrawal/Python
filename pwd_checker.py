"""
Password Strength Checker
Checks whether a password is weak, medium, or strong

#LOGIC with simple input 
pwd= input("Enter Password:")
strenght=0
if len(pwd)>=8 :
    strenght+=1
if any(char.isupper()for char in pwd):
    strenght+=1
if any(char in"@#$%^&*!" for char in pwd):
    strenght+=1

if strenght<=1:
    print("weak")
elif strenght==2:
    print("medium")
else :
    print("strong")

"""
#With Function 

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*" for char in password):
        strength += 1

    if strength <= 1:
        return "Weak "
    elif strength == 2:
        return "Medium "
    else:
        return "Strong "

pwd = input("Enter your password:")
print("Pwd Strength:",check_strength(pwd))


        