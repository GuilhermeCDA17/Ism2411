#Reflection
# 1. After learning about how lists work in Pyhton, I was really surprised by how easy it is to edit these lists afterwards. As normally it's very hard to change variables afterwards in previous assignments.
# 2. In high school, I had to do a project comparing the passer rating of various quarterbacks when they would pass deep. In this project I had a really hard time calculating the average of the passer rating as I had to put every rating in the calulcator to get the number I wanted. But now, I can easily copy the list and automatically get the number I need.

#Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

#Exercise 2

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

#Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#Exercise 5

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because it's not possible to accidentaly change their values.")

print(coords)

#Exercise 6

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)

#Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = price * 0.90
    discounted.append(round(new_price, 2))

print(prices)
print(discounted)

#Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

count = len(high_sales)
average = sum(high_sales) / count

print(high_sales)
print("Count:", count)
print("Avg:", round(average, 2))