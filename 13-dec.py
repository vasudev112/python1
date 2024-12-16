# Function to calculate sum of all prices
def sum_of_prices(prices):
    return sum(prices)

n = int(input("How many prices do you want to enter? "))
prices = []

for i in range(n):
    price = float(input(f"Enter price {i + 1}: $"))
    prices.append(price)
total_sum = sum_of_prices(prices)
print(f"The total sum of all prices is: ${total_sum:.2f}")
