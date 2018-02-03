SpecialSym=['$','@','!','*']
while True:
    password= input("Hit a password :")
    if len(password)< 6:
        print("The password length should be in between 6-16 characters")
        continue
    elif len(password)> 16 :
        print("The password length should be not be > 16")
        continue
    elif not any(char.isdigit() for char in password):
        print('The password should contain atleast one number')
        continue
    elif not any(char.isupper() for char in password):
        print('The password should contain atleast one uppercase letter')
        continue
    elif not any(char.islower() for char in password):
        print('The password should contain atleast one lowercase letter')
        continue
    elif not any(char in SpecialSym for char in password):
        print('The password should contain atleast 1 of the following symbols $@#!')
        continue
    else :
        print("Password that you have entered is correct")
        print(password)
        break