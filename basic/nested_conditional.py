name = "m"
if(len(name)==0):
    print("Failed")
else:
    if(len(name)<2):
        print("The name length must be minimum 2")
    else:
        print("Success") 


name1 = "md" 
if(len(name1)==0):
    print("Failed")
else:
    if(len(name1)<2):
        print("The name length must be minimum 2")
    else:
        print("Success")   


name3 = "soibal" 
phone = "0"
email = "m"
if(len(name3)==0 or len(phone)==0 or len(name)==0):
    print("You have to fill up the gap")
else:
    if(len(name3)<2):
        print("The name length must be minimum 2")
    elif(len(phone)!=11):
        print("The phone number size must be equal to 11")
    else:
        print("Success")    






name4 = "soibal"
phone1 = "01758128814"
email1 = "m"
if(len(name4)==0 or len(phone1)==0 or len(email1)==0):
    print("You must be fill up the gap")
else:
    if(len(name4)<2):
        print("The name length must be minimum 2")
    elif(len(phone1)!=11):
        print("The phone number must be equal to 11")
    else:
        print("SUCCESS")          





name5 = "salman5"
phone2 = "01758128814"
email2 = "md"
if(len(name5)==0 or len(phone2)==0 or len(email2)==0):
    print("You must be fill up the gap")
else:
    if(len(name5)<2 or len(name5)>6):
        print("The name length must be between 2 and 6")
    elif(len(phone2)!=11):
        print("The phone number must be equal to 11")
    else:
        print("Success")                                  