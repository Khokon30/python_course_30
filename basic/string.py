name = "Md Moniruzzaman Konok"
size = len(name)
print(size)
name1 = "Moniruzzaman"
size1 = len(name1)
print(size1)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
print(name[13])
print(name[14])
print(name[15])

#string slicing

print(name[0:])
print(name[5:16])
print(name[:16])
print(name[17:])
print(name[16:])

# string methods

name2 = "md moniruzzaman konok"
print(name2.upper())
name3 = "MD MONIR HOSSAIN"
print(name3.lower())
name4 = "monir hossain"
print(name4.capitalize())
name5 = "konok"
print(name5.capitalize())
name6 = "monir"
print(name6[0].isupper())
print(name6[0].islower())

name7 = "Moniruzzaman"
print(name[0].isupper())


name8 = "Md Monir"
check_upper = name8[0].isupper()
if(check_upper):
    print("The first letter is capital")
else:
    print("The first letter is not capital")    

name9 = "konok"
check_lower = name9[0].islower()
if(check_lower):
    print("THE FIRST LETTER IS LOWER")
else:
    print("THE FIRST LETTER IS NOT LOWER")      


name10 = "MONIRUZZAMA"
check_lower = name10[5].islower()
if(check_lower):
    print("The 6th letter is lower")
else:
    print("THE 6TH LETTER IS CAPITAL") 

#looping

for i in range(6):
    print(i)
for i in range(2,50):
    print(i)  

for i in range(0,10,2):
    print(i)  
    
for i in range(5,51,5):
    print(i)

for i in range(0,100,12):
    print(i)  

name13 = "khokon" 
for i in range(len(name13)):
    print(i)

num = "Monir"
for i in range(len(num)):
    print(num[i])

name25 = "MD MONIRUZZAMAN KONOK"
for i in range(len(name25)):
    print(name25[i])    

name0 = "Md Monir Hossain"
for i in range(len(name0)):
    print(name0[i])    