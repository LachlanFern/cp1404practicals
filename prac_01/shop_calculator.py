item_amount = int(input("Number of items: "))
total_cost = 0

while item_amount < 0:
    print("Invalid number of items!")
    item_amount = int(input("Number of items: "))

for i in range(item_amount):
    item_cost = float(input("Price of item: "))
    total_cost += item_cost



if total_cost > 100:
    total_cost *= 0.9

print(f"Total price for {item_amount} items is ${total_cost:.2f} ")


