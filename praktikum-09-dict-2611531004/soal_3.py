rooms = {"IF101": "Lab 1", "IF102": "R. 204", "IF103": "R. 301"}
codes = input("Course codes: ").split()
 
for code in codes:
    if code in rooms:
        room = rooms[code]
        print(code, "->", room)
    else:
        print(code, "-> not found")