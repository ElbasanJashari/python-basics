store = {
    "Electronics": {
        "Laptop": 1200,
        "Phone": 800,
        "Tablet": 450,
        "Headphones": 200
    },
    "Clothing": {
        "Jacket": 150,
        "Shoes": 210,
        "Jeans": 80,
        "Hoodie": 95
    },
    "Food": {
        "Coffee": 25,
        "Chocolate": 12,
        "Tea": 18,
        "Nuts": 30
    }
}


def bestseller(category):
    categories = store[category]
    return max(categories, key=categories.get)


def category_total(category):
    total = sum(store[category].values())
    return total


def store_report():
    for category in store:
        print(f"{category} | Best Seller: {bestseller(category)} | Category Total: {category_total(category)}")

    biggest_category = max(
        store, key=lambda category: category_total(category))
    print("Biggest category by revenue: ", biggest_category)

    all_products = {}
    for category in store:
        for product, price in store[category].items():
            all_products[product] = price

    cheapest_product = min(all_products, key=all_products.get)
    print("Cheapest product across entire store: ", cheapest_product)

    most_expensive_product = max(all_products, key=all_products.get)
    print("Most expensive product across entire store: ", most_expensive_product)


store_report()
