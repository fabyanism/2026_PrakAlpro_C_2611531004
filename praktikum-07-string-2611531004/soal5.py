# Name: FABIAN ALHADI ZALINOV
# NIM: 2611531004
# Question 5

username = input("Username: ")
if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

nim = input("Masukkan NIM: ")
if len(nim) == 10 and nim.isdigit():
    print("Valid, intake year 20" + nim[:2])
else:
    print("Invalid NIM")