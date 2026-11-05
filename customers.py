# 1. I would use .get() when a key is missing and that's okay, like an optional field such as a email or phone number.
# It lets me get a default value so the program keeps running.
# I would use bracket notation when the key must exist, due to a KeyError tells me right away that something is wrong with the info. My rule of thumb is that use .get() for optional data, brackets for required data.
#
# 2. It reminds me of a PivotTable in Excel, where you total the amounts for each region. 
# The Python version is more useful for latge datasets because it reads the data one row at a time, runs the same way everytime, and can handle more rows than Excel.




#---Exercise 1---
print("=== Exercise 1: One customer ===")
customer = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print("name:", customer["name"])
print("email:", customer["email"])
print("tier:", customer["tier"])
print("ytd_spend:", customer["ytd_spend"])
print(customer)

#---Exercise 2---
print("\n=== Exercise 2: Update and add ===")
customer["phone"] = "813-555-0101"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)

#---Exercise 3---
print("\n=== Exercise 3: Safe lookup ===")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")

#---Exercise 4---
print("\n=== Exercise 4: Iterate ===")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dict without .items() gives only the KEYS, not the values.
print("Without .items():")
for key in customer:
    print(key)

#---Exercise 5---
print("\n=== Exercise 5: Lookup table ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
purchase = 200
final_price = purchase * (1 - discount)
print(f"Tier: {tier}")
print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")

#---Exercise 6---
print("\n=== Exercise 6: List of dicts ===")
customers = [
    {"name": "Alice Johnson", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 3200.00},
    {"name": "Bob Smith", "email": "bob@example.com", "tier": "silver", "ytd_spend": 640.25},
    {"name": "Carla Gomez", "email": "carla@example.com", "tier": "bronze", "ytd_spend": 120.00},
]

purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount: ${discount_amount:.2f}")

#---Exercise 7---
print("\n=== Exercise 7: Nested catalog ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} has only {details['stock']} left")

#---Exercise 8---
print("\n=== Exercise 8: Sales by region ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")