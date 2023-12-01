
string = "Md Moniruzzaman Konok"
#count = 0

# for i in string:
#     print(i)
#     count = count + 1

# print(count)    


def custom_len():
    count = 0
    for i in string:
        count = count + 1 
    print(count)
    return count   
a = custom_len()  
print(a) 


name = "Md Monir Hossain"
name2 = "Md Suruzzaman"
name3 = "SK Alamin"
name4 = "Jannatul Ferdous"

def custom_len(a,b,c,d):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in a:
        count1 =count1+1
    for j in b:
        count2 = count2+1
    for k in c:
        count3 = count3+1
    for l in d:
        count4 = count4+1
    return count1,count2,count3,count4

w,p,y,z = custom_len(name,name2,name3,name4)
print(w,p,y,z)  


name5 = "Bangladesh is my mother land. Bangladesh is a beautiful country in the modern world.But here we cannot live with peace."

def custom_len(n):
    count = 0
    for i in n:
        count = count + 1
    return count
x = custom_len(name5)
print(x)    
