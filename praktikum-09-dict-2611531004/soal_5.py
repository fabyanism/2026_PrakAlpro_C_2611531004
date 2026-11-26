n = int(input("Jumlah setoran: "))

totals = {}

for i in range(n):
    data = input().split()

    name = data[0]
    amount = int(data[1])

    if name not in totals:
        totals[name] = 0

    totals[name] += amount

for name, total in totals.items():
    print(name + ":", total)

total_cash = sum(totals.values())
print("Total cash:", total_cash)

top_name = max(totals, key=totals.get)
print("Top contributor:", top_name, "(" + str(totals[top_name]) + ")")