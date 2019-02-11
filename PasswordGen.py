from random import randint

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
length = int(input("How long do you want the password?"))

password = ""
for num in range(length - 2):
    if randint(0,4) == 1:
        password += ALPHABET[randint(0,25)].upper()
    else:
        password += ALPHABET[randint(0,25)]
password += str(randint(10,99))
        
print(password)
