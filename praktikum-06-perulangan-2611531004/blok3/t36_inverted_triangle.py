height = int(input("Masukkan tinggi: "))

for row in range (height, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()