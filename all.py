import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data (since your dataset is large/unstructured)
products = ["Camera", "Headphones", "Laptop", "Monitor", "Phone", "Printer", "Tablet"]
sales_product = np.random.randint(30000000, 40000000, size=7)

categories = ["Accessories", "Electronics", "Office"]
sales_category = [33.3, 32.9, 33.9]

cities = ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Mumbai"]
profit_city = np.random.randint(7000000, 9000000, size=5)

payment_methods = ["CARD", "UPI", "NETBANKING", "CASH"]
payment_values = [24.5, 25.4, 23.9, 26.1]

channels = ["Distributor", "Online", "Retail"]
profit_channel = np.random.randint(13000000, 15000000, size=3)

salesrep = ["Amit", "John", "Neha", "Priya", "Ravi", "Sara"]
salesrep_perf = np.random.randint(38000000, 42000000, size=6)

discount = np.linspace(0.01, 0.30, 30)
sales_discount = np.random.randint(80000, 180000, size=30)

quantity = np.arange(1, 11)
sales_quantity = quantity * 40000 + np.random.randint(10000, 50000, size=10)

order_status = ["Pending", "Completed", "Cancelled"]
order_values = [33.5, 33.0, 33.4]

# Create figure
plt.figure(figsize=(15, 10))

# 1 Sales by Product
plt.subplot(3, 3, 1)
plt.bar(products, sales_product)
plt.title("Sales by Product")
plt.xticks(rotation=45)

# 2 Sales by Category
plt.subplot(3, 3, 2)
plt.pie(sales_category, labels=categories, autopct='%1.1f%%')
plt.title("Sales by Category")

# 3 Profit by City
plt.subplot(3, 3, 3)
plt.bar(cities, profit_city)
plt.title("Profit by City")
plt.xticks(rotation=45)

# 4 Payment Method
plt.subplot(3, 3, 4)
plt.pie(payment_values, labels=payment_methods, autopct='%1.1f%%')
plt.title("Payment Method")

# 5 Profit by Channel
plt.subplot(3, 3, 5)
plt.bar(channels, profit_channel)
plt.title("Profit by Channel")

# 6 SalesRep Performance
plt.subplot(3, 3, 6)
plt.bar(salesrep, salesrep_perf)
plt.title("SalesRep Performance")
plt.xticks(rotation=45)

# 7 Discount vs Sales
plt.subplot(3, 3, 7)
plt.plot(discount, sales_discount)
plt.title("Discount vs Sales")
plt.xlabel("Discount")

# 8 Quantity vs Sales
plt.subplot(3, 3, 8)
plt.scatter(quantity, sales_quantity)
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")

# 9 Order Status
plt.subplot(3, 3, 9)
plt.pie(order_values, labels=order_status, autopct='%1.1f%%')
plt.title("Order Status")

plt.tight_layout()
plt.show()