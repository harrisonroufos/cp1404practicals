DISCOUNT = 0.9
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
total_cost_of_items = 0
for item in range(number_of_items):
    cost_of_item = float(input("Price of item: "))
    total_cost_of_items = total_cost_of_items + cost_of_item

if total_cost_of_items >= 100:
    total_cost_of_items = total_cost_of_items * DISCOUNT

print(f"Total price for {number_of_items} is: ${total_cost_of_items:.2f}")
