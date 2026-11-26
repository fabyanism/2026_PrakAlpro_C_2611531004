students = input("Daftar nomor absen: ").split()
submitted = input("Daftar nomor absen yang sudah mengumpulkan: ").split()

submitted_set = set(submitted)
students_set = set(students)

submitted_set = submitted_set & students_set
not_submitted = students_set - submitted_set

print("Submitted: ", len(submitted_set), "students")
print("Not Submitted: ", len(not_submitted), "students")

for student in students:
    if student in not_submitted:
        print(student)