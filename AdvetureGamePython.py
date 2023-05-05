import random
import time


def print_pause(msg, amount_of_time=2):
    print(msg)
    time.sleep(amount_of_time)


def intro():
    print_pause(
        "You find yourself standing in an open field"
        ", filled with grass and yellow wildflowers.",
        3,
    )
    print_pause(
        "Rumor has it that a wicked fairie is somewhere around here"
        ", and has been terrifying the nearby village.",
        3,
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty"
        "(but not very effective) dagger."
    )


def house_intro(enemy_name, sword):
    print_pause(f"You approach the door of the house.")
    print_pause(
        "You are about to knock when the door"
        f" opens and out steps a {enemy_name}."
    )
    print_pause(f"Eep! This is the {enemy_name}'s house!")
    print_pause(f"The {enemy_name} attacks you!")
    if sword is False:
        print_pause(
            "You feel a bit under-prepared for this"
            ", what with only having a tiny dagger.",
            1,
        )
    else:
        print_pause(
            "You feel prepared for this, with the sword"
            " that you just had from the cave.",
            1,
        )


def player_choice(stages, sword):
    print_pause("\nEnter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave")
    while True:
        choice = input("What would you like to do ?\n (Please Enter 1 or 2.)")
        if choice.isnumeric():
            if int(choice) == 1:
                stage = random.choice(stages)
                stage(sword, stages)
                break
            elif int(choice) == 2:
                cave_stage(sword, stages)
                break
            else:
                print_pause("Please Enter 1 or 2 to proceed")
        else:
            print_pause("Please Enter 1 or 2 to proceed")


def pirate_stage(sword, stages):
    house_intro("pirate", sword)
    choice = check_player_answer()
    return fight(sword, choice, "pirate", stages)


def gorgon_stage(sword, stages):
    house_intro("gorgon", sword)
    choice = check_player_answer()
    return fight(sword, choice, "gorgon", stages)


def troll_stage(sword, stages):
    house_intro("troll", sword)
    choice = check_player_answer()
    return fight(sword, choice, "troll", stages)


def cave_stage(sword, stages):
    if sword is not True:
        sword = True
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave..")
        print_pause("Your eye catches a glint of"
                    " metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        print_pause("You walk back out to the field.")

    else:
        print_pause(
            "You've been here before, and gotten all the"
            " good stuff. It's just an empty cave now."
        )
        print_pause("You walk back out to the field.")

    return player_choice(stages, sword)


def fight(sword, choice, enemy_name, stages):

    if choice == 1:
        if sword is False:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for"
                        f"the {enemy_name}.")
            print_pause("You have been defeated", 3)

        else:
            print_pause(
                f"As the {enemy_name} moves to attack,"
                " you unsheath your new sword."
            )
            print_pause(
                "The Sword of Ogoroth shines brightly in your hand"
                " as you brace yourself for the attack."
            )
            print_pause(
                f"But the {enemy_name} takes one look at"
                " your shiny new toy and runs away!."
            )
            print_pause(
                f"You have rid the town of the {enemy_name}."
                " You are victorious!"
            )

    else:
        print_pause(
            "You run back into the field. Luckily,"
            " you don't seem to have been followed.",
            3,
        )
        return player_choice(sword, stages)


def check_player_answer():
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice.isnumeric() is True:
            if int(choice) == 1 or int(choice) == 2:
                return int(choice)
            else:
                print_pause("Please enter 1 or 2 to proceed")


def main():
    sword = False
    stages = [pirate_stage, gorgon_stage, troll_stage]
    intro()
    player_choice(stages, sword)


main()

while True:
    y = input("Do you want to play again ?(y/n)")
    if y == "y":
        main()
    elif y == "n":
        break
    else:
        print("Please enter y or n ")
