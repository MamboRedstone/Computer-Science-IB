Num = []

for i in range(3):
    number = int(input(f"Enter number {i+1}: "))
    Num.append(number)

print(f"The average of the 3 numbers is: {sum(Num)/3}\n")

name = input(f"Enter your name: ")
age = int(input(f"Enter your age: "))

print(f"{name} in 10 years you will be {age+10} years old\n")

Valid = False

while not Valid:
    number = input("Enter a 3 digit number: ") 
    if len(number) == 3:
        Valid = True 
    else:
        print("The number must be 3 digits.") 

