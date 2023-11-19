
list = ["apple","banana","cherry","mango"]
j = list.pop(2)          #pop method = removes the element at the specified position.
print(j)
print(list)
list1 = ["jackfruit","mango","lichi"]
x = list1.pop(0)
print(x)
print(list1)

list2 = ["cocunut","pine apple","date"]
list2.remove("pine apple")  # remove method = removes the item with the specified value.
print(list2)

list3 = ["Rakib","Konok","Monir","Azizul"]
list3.remove("Monir")
print(list3)

list4 = ["apple","banana","mango","lichi","Rakib","Konok"]
list4.reverse()
print(list4)

def myFunc (e):
    return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True , key=myFunc)
print(cars)

list5 = ["ms","bmw","honda","pazaru","microbus"]
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)
def myFunc (e):
    return len(e)
list5.sort(reverse = True , key = myFunc)
print(list5)

list6 = ["apple","banana","mango","lichi","Rakib","Konok",85,785,14]
l = list6.index("Konok")
print(l)
m = list6.index(785)
print(m)

fruits = ["banana","mango","jackfruit","lichi"]
cars = ["bmw","pazaru","bus","truck","microbus","auroplane"]
fruits.extend(cars)
print(fruits)

fruits_cars =  ["banana","mango","jackfruit","lichi","bmw","pazaru","bus","truck","microbus","auroplane"] 
points = [1,2,3,4,5,6,7,8,9,147,7845, 9,9654123]
fruits_cars.extend(points)
print(fruits_cars)