# Name: FABIAN ALHADI ZALINOV
# NIM: 2611531004
# Question Bonus

kalimat = input("Masukkan kalimat: ")
teks = kalimat.replace(" ", " ").lower()
if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")