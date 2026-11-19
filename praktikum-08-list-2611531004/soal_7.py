menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3

sales = [
    [15, 12, 12],
    [13, 14, 10],
    [12, 12, 14]
]

for i in range(number_of_days):
    for j in range(len(menus)):
        print(f"Day {i + 1}, {menus[j]}: {sales[i][j]}")

print("\nTotal per day:")
for i in range(number_of_days):
    daily_total = 0
    for j in range(len(menus)):
        daily_total += sales[i][j]
    print(f"Day {i + 1}: {daily_total}")

menu_totals = []

for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total += sales[i][j]
    menu_totals.append((menus[j], menu_total))

print("\nTotal per menu:", menu_totals)

best_name = ""
best_total = 0

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")