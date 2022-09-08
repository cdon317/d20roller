import random as ra

# function to answer stat roll question:
def answer_stat_roll():
    """Answers first question on whether player wishes to roll for stats."""

    game = True

    while game:
        # noinspection PyBroadException
        try:
            response = input("Would you like to roll for character stats?: ")
            if response in ["Yes", "yes", "Y", "y"]:
                print("Rolling...")
                print("Your player stats are: ")
                return player_stats()
            elif response in ["No", "no", "N", "n"]:
                break
            else:
                print("Please enter 'yes' or 'no.'")
                continue
        except:
            print("Please enter 'yes' or 'no.'")
            game = False
            continue

    return ''

# function to roll 6 character stats:
def player_stats():
    """Uses user inputs to provide values for player to assign to stats."""

    stat_rolls = []

    for i in range(6):
        buffer = []
        for j in range(4):
            num = ra.randint(1, 6)
            buffer.append(num)
        buffer.remove(min(buffer))
        total = sum(buffer)
        stat_rolls.append(total)

    return stat_rolls

# function to get random numbers for dice rolls
def roll(f, n):
    """Uses user inputs f(number of faces) and n(number of dice) to return list L."""

    print("Rolling...")

    rolls = []
    f = int(f[1:])

    for die in range(n):
        dice_roll = ra.randint(1, f)
        rolls.append(dice_roll)

    return rolls

# character stat creation:
print(answer_stat_roll())

# main dice-rolling program:
faces = input("Which dice would you like to roll? d4, d6, d8, d10, d12, or d20: ")
num_dice = input("How many dice would you like to roll? (1-10): ")
dice_result = roll(str(faces), int(num_dice))
print(dice_result)
