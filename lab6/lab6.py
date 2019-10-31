# James Park
# 31 October 2019
# Lab #6 dictionary

rooms = {}
instructors = {}
times = {}

# Insert rooms values
rooms["CS101"] = "3004"
rooms["CS102"] = "4501"
rooms["CS103"] = "6755"
rooms["NT110"] = "1244"
rooms["CM241"] = "1411"

# Insert instructor values for same keys
instructors["CS101"] = "Haynes"
instructors["CS102"] = "Alvarado"
instructors["CS103"] = "Rich"
instructors["NT110"] = "Burke"
instructors["CM241"] = "Lee"

# Insert times values
times["CS101"] = "8:00 am"
times["CS102"] = "9:00 am"
times["CS103"] = "10:00 am"
times["NT110"] = "11:00 am"
times["CM241"] = "1:00 pm"

# User prompt
while True:
    print("Inputs are case sensitive. type 'x' to exit.")
    uInput = input("Course number:")
    if uInput == "x":
        print("Exiting")
        break
    if uInput in rooms and uInput in instructors and uInput in times:
        print("Room #:", rooms[uInput])
        print("Instructor:", instructors[uInput])
        print("Meeting time:", times[uInput])
    else:
        print("invalid input. Try again.")
