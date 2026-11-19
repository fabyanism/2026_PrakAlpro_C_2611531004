LAST_DIGIT = 4
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = [31500, 42000, 33500, 36500, 29000, 38500, 34500]

for i in range(7):
    print(f"Day {i + 1}: {expenses[i]}") 

total = 0
for expense in expenses:
    total += expense

average = total / 7

highest = expenses[0]
highest_day = 1

for i in range(7):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

above_limit = 0
for expense in expenses:
    if expense > daily_limit:
        above_limit += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", above_limit)