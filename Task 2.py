Valid = False

while not Valid:
    username = input("Enter your username: ")
    if len(username) < 6:
        print("Incorrect length")
    elif username[-2] != "_":
        print("Missplaced or no _")
    else:
        Valid = True

if username[-1] == "S":
    print(f"You are a student in year {username[:2]}\nInitial: {username[2]}\nName: {username[3:-2]}")
elif username[-1] == "T":
    print("You are part of staff as a teacher")
elif username[-1] == "A":
    print("You are part of staff as a admin")