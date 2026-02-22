# Shopping list maker

shopping_list = []
num_of_items = int(input("How many items would you like to add? "))

for items in range(num_of_items):
    item = input("Write the product you will buy: ")
    shopping_list.append(item)

print("\nThe list of products to buy:")
for product in shopping_list:
    print("- " + product)
