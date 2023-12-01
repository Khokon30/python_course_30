
car ={"name":"Pazaru","model":"M1","color":"Mat Black","price":1000000}
print(car['name'])
print(car.get('price'))
print(car.keys())
print(car.values())
print(car.items())

for i in car:
    print(i)  # only keys 
for i in car.values():
    print(i)  # only values
for i,j in car.items():
    print(i,j)  # both keys and values  

cars = {"car1":{"name":"Toyeta","model":"A50","color":"White","price":10000000},
        "car2":{"name":"Bajaj","model":"135cc","color":"Red","price":150000},
        "info":{"name":"Abdur Rahman","birth_date":"10/10/1996","address":"Sadarpur","SSC_GPA":5.00,"HSC_GPA":5.00,"B.A_GPA":3.23,"M.A_GPA":3.12}}

for i,j in cars.items():
    for k in j.items():
        print(i,k)
          