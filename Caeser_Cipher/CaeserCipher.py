def encrypt(text,s):
    result = ""
    # transverse the plain text
    for char in text: 
        if char == '?' or char == '.' or char == ',':
            result = result + char
        elif char == ' ':
            result = result + char
        elif char.isupper():
            result = result + chr((ord(char) + s - 65) % 26 + 65)
        else:
            result = result + chr((ord(char) + s - 97) % 26 + 97)
    return result
#check the above function

def decrypt(text,s):	
    result = ""
     # transverse the plain text
    for char in text: 
        if char == '?' or char == '.'  or char == ',':
            result = result + char
        elif char == ' ':
            result = result + char
        elif char.isupper():
            result = result + chr((ord(char) - s - 65) % 26 + 65)
        else:
            result = result + chr((ord(char) - s - 97) % 26 + 97)
    return result

i = 1
while(i):
    choice= int(input("\nPlease press 1 for encryption or 2 for decryption: "))
    if choice==1:
            text = input("\nEnter the Plain Text: ")
            s = int(input("Enter the Shift Pattern: "))
            # print ("\nPlain Text : " + text)
            # print ("Shift pattern : " + str(s))
            print ("Cipher Text: " + encrypt(text,s))
    elif choice==2:
            ck = input("Enter the Cipher Text:\n")
            s = int(input("Enter the Shift Pattern: "))
            print ("Original Plain Text: " + decrypt(ck,s)) 
           
    else:
            print("Wrong choice entered. Exiting now..")
            exit()      
    con = int(input("\nDo you want to continue? (press 1 for YES/press 2 for NO):"))
    if con == 1:
        continue
    else:
        exit()
