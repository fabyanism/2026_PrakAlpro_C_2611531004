# Name: FABIAN ALHADI ZALINOV
# NIM: 2611531004
# Question 7

name = "Fabian Alhadi Zalinov"
nim = "2611531004"
space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]
username = first_name.lower() + nim[-3:]
intake_year = "20" + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name:':<10}{name.title()}")
print(f"{'NIM:':<10}{nim}")
print(f"{'Username:':<10}{username}")
print(f"{'Intake Year:':<10}{intake_year}")
print("=" * 30)