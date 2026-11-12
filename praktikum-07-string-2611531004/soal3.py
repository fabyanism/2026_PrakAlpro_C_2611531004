# Name: FABIAN ALHADI ZALINOV
# NIM: 2611531004
# Question 3 (A)

text = "Informatika"
print(text[11])
print(text.upper())
print(text[0:10])

# Question 3 (B)

text = "Fabian Alhadi Zalinov"
count = 0
for char in text:
    if char in "aiueoAIUEO":
        count += 1
print("Vowels:", count)