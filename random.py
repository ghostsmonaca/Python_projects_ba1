name = ""
gender = ""
items = []


def start():
    print("Hello traveler! Welcome to the realm of fantasy.")
    name = input("What is your name, dear one?")
    print(f"Nice to meet you {name}.")
    print("What pronouns should we use for you?")
    print("Please enter the number corresponding with your preferences.")
    print("1. She/Her")
    print("2. He/Him")
    print("3. They/Them")
    print("4. It/Its")
    gender = int(input("The number: "))
    match gender:
        case 1:
            gender = "Female"
        case 2:
            gender = "Male"
        case 3:
            gender = "Nonbinary"
        case 4:
            gender = "Thing"
    print(f"Perfect! Your pronouns have been set to: {genderPronoun(gender)}")
    stage_one()


def stage_one():
    print("")
    print("We shall now start with the story.")
    input()
    print(
        "Imagine you wake up in a dark forest, it is cold and you're wearing nothing but a simple t-shirt, sweatpants and some simple sneakers."
    )
    input()
    print(
        "There is nothing you can hear or see. You have a small backpack on you, inside you find: "
    )
    print(backpack(1))
    input()


def backpack(stage):
    if stage == 1:
        items.append("Flashlight")
        items.append("Towel")
        items.append("25 Gold")
        return items
    else:
        return items


def genderPronoun(gender):
    match gender:
        case "Female":
            return "She Her"
        case "Male":
            return "He Him"
        case "Nonbinary":
            return "They Them"
        case "Thing":
            return "It Its"


stage_one()
