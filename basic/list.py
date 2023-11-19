list = [12,78,14,75,9,19,113,50,1,2,3,55,110]
print(list)
print(len(list))
print(list[4])
print(list[0:6])

sum= 0
for i in range(len(list)):
    sum = sum + list[i]
print(sum)

list1 = [10,3,45,78]
sum1 = 0
for a in range(len(list1)):
    sum1 = sum1 + list1[a]
print(sum1) 

list2 = [1,2,3,45,40,86,200,60,456]
sum2 = 0
for b in list2:
    sum2 = sum2 + b
print(sum2) 

list3 = [12,39,58,940,1,999,550]
sum3 = 0
for c in list3:
    sum3 = sum3 + c
print(sum3) 


list4 = [101,148,78,41,1,2,4,5,6,51,123,11]
list4.append(7878)                          # append method = add one value as a last index.
print("after append", list4)

list4.clear()                   # clear method = clear all value from the list.
print("after clear", list4)

list5 = list1.copy()
print("after copy",list5)

list6 = list.copy()
print("after copy", list6)


list7 = [12,47,89,1,2,1,2,14,14,45,1,2,3,1,14]
n = list7.count(14)
print(n)
j = list7.count(1)
print("after count", j)


list7.count(1)

count = 0
for k in list7:
    if (k==1):
        count = count + 1 
    else:
        count = count
print(count) 


list8 = [4,5,7,4,5,4,4,4,4,5,14,125]
k = list8.count(4)

count = 0
for l in list8:
    if (l == 4):
        count = count + 1
    else:
        count = count
print(count)  


list9 = [147,45,14,78,50,96,69,87,9,12,3,7,8,99]
even_list = []
odd_list = []

for n in list9:
    if( n%2==0):
        even_list.append(n)
    else:
        odd_list.append(n)

print(even_list) 
print(odd_list) 

list10 = [10,12,7,9,77,99,12,24,36,1,3,5,2,4,6,8]

even_list1 = []
odd_list1 = []
for d in list10:
    if(d%2==0):
        even_list1.append(d)
    else:
        odd_list1.append(d)
print(even_list1)
print(odd_list1)  

list11 = [12,1,5,45]
list11.insert(0,4)
print(list11)
list11.insert(2,458751414)
print(list11)
    

  