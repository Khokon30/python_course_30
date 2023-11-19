print("This is our first python code")
print(10)

product_name = "sugar"
print("The name of the product is",product_name)
print(type(product_name))
product_name1 = "187"
print(type(product_name1))
product_name2 = 47854
print(type(product_name2))
product_name3 = 457.1244254758
print(type(product_name3))



goods_name1 = "sugar"
goods_name2 = "egg"

quan1 = 10
quan2 = 6

price1 = 150
price2 = 50

total_price1 = price1 * quan1
total_price2 = price2 * quan2

discount = 14

total_cost = total_price1 + total_price2
discount_price = (total_cost * discount)/100
total_cost_after_discount = total_cost - discount_price

print(total_cost,discount_price,total_cost_after_discount)

total_cost_after_discount2 = total_cost - (total_cost * discount)/100
print(total_cost_after_discount2)


print(total_price1,total_price2)