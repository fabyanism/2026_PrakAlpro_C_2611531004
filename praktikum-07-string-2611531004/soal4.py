# Name: FABIAN ALHADI ZALINOV
# NIM: 2611531004
# Question 4

phone = "082611531004"
jumlah_bintang = len(phone) - 7
masked = phone[:4] + "*" * jumlah_bintang + phone[-3:]
print(masked)