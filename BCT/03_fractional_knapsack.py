
items = []

n = int(input("Enter number of items: "))

for i in range(n):
    value, weight = map(float, input(
        f"Enter value and weight of item {i+1}: "
    ).split())

    if weight <= 0:
        print("Weight must be positive")
        exit()

    ratio = value / weight
    items.append((ratio, value, weight))

capacity = float(input("Enter knapsack capacity: "))

# Sort according to highest value/weight ratio
items.sort(reverse=True)

total_value = 0

for ratio, value, weight in items:

    if capacity <= 0:
        break

    taken = min(capacity, weight)

    total_value += taken * ratio
    capacity -= taken

print(f"Maximum value = {total_value:.2f}")
