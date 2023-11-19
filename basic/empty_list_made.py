# list = [ "ab", "cd", "ef" ]
# res = []
# for i in list:
#     res.extend(ord(num) for num in i )
# print  ("The ascii value of list is : " + str(res))   

# list1 = ['jf','Bd']
# for a in list1:
#     for k in a:
#         asc = ord(k)
#         print(asc)

# list2 = ['aBc','DeF','gHi','JkL']

# list3 = []
# list4 = []
# for i in list2:
#     for r in i:
#         asc = ord(r)
#         list3.append(asc)
#         list4.append(asc)
# print(list3)  
# print(list4)  


list = ['ab','cd','ef']

list_1 = []

sum = 0

for a in range(len(list)):
    for b in range(len(list[a])):
        asc = ord(list[a][b])
        sum = sum + asc
        list_1.append(asc)


print(list_1)
print(sum)
        


