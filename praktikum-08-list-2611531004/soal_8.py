number_of_rows = 4
seats_per_row = 5

cinema = []
for i in range(number_of_rows):
    row = []
    for j in range(seats_per_row):
        row.append(".")
    cinema.append(row)

seats_taken = 0

while True:
    for i in range(number_of_rows):
        print(f"Row {i + 1}:", end=" ")
        for j in range(seats_per_row):
            print(cinema[i][j], end=" ")
        print()

    row_number = int(input("Row (0 to stop): "))

    if row_number == 0:
        break

    seat_number = int(input("Seat: "))

    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif cinema[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        cinema[row_number - 1][seat_number - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

print("Seats taken:", seats_taken)