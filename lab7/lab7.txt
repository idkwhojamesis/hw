# James Park
# Prof. Kounavelis
# Lab #7 Password check

def passCheck(pw):
    specialChars = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")"}
    if (len(pw) >= 10) and (c.isupper() for c in pw) and any(c.isdigit() for c in pw) and any((c in specialChars) for c in pw):
        print("VALID Password")
    else:
        print("INVALID Password!")
    
passStr = input("Enter a password :")
passCheck(passStr)
