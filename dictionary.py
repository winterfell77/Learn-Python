monthConversions = {
    "Jan": "Janurary",
    "feb": "Feburary",
    "mar": "march",
}
print(monthConversions["Jan"])

friends = ["jan", "feb", "mar"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

number_grid = [
    [8, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)

try:
    number = int(input("Enter a number: "))
    print(number)


except ZeroDivisionError:
    print("Divided by zero")
except:
    print("Invalid Input")


open("employees.txt", "r")
open()