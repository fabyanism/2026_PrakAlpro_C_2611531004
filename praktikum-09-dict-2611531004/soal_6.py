schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day = max(schedule, key=lambda day: len(schedule[day]))
count = len(schedule[busiest_day])

print("Busiest day:", busiest_day, f"({count} courses)")

course = input("Course name: ")

days = 0
for day in schedule:
    if course in schedule[day]:
        days += 1

print(f"{course}: {days} days")