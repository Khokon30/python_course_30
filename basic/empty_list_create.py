
list = [ 'ab','cd','ef']

list_2 = []
sum = 0
for i in list:
     for k in i:
             asc = ord(k)
             sum = sum + asc
             list_2.append(asc)

print(list_2)
print(sum)  


list3 = [ 'AbC','dEf','KoNoK' ]

list_4 = []
sum = 0

for y in range(len(list3)):
       for w in range(len(list3[y])):
              asc = ord(list3[y][w])
              list_4.append(asc)
              sum = sum + asc

print(list_4)
print(sum)              

