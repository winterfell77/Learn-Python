print("Hello World")

print("afsdfasdf")

character_name = "john"
character_age = "35"

print("there once was a man named " + character_name)
print("he was " + character_age + " years old")
print("allen\nshen")
print("allen\"shen")  # escape characters(comment)

print(character_name.upper())
print(character_name.isupper())
print(character_name.index("o"))

print(str(5) + "asdfa")

# name = input("enter your name:")

friends = ["Kevin", "karen", "jim"]
numbers = [3, 4, 5, 3, 3]
print(friends)
print(friends[0])
friends.extend(numbers)
friends.append("creed")
friends.remove("karen")
print(friends)
friends.clear()
print(friends)

coordinates = (4, 5)
print(coordinates[0])


def sayhi(name):
    print("hello user" + name)


sayhi("name");


if character_name == "john":
    print("yes")


print(type(character_name))