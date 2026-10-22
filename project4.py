import random
import time

health = 4
treasure = 0
safety_chance = 0
healing_chance = 0
# This is for starting the treasure bonus values for each door
four_t_bonus = 0
three_t_bonus = 0
two_t_bonus = 0
# This is for starting the safety bonus values for each door
four_s_bonus = 0
three_s_bonus = 0
two_s_bonus = 0
# This is for total healing bonus
healing_bonus = 1
rounds = 10
treasure_multiplier = 1
monster_damage = 1

print("You've made it to the Dungeon of Doors! Spooky! Pick your choices wisely, and don't get eaten!")
time.sleep(.25)
print("Behind each door is either a heal, treasure, or a monster. Each door has a higher chance of getting a monster than the last, but rewards good luck with more treasure.")

# This is a for loop - This loop loops lines 27 to 249
for i in range(10):
    time.sleep(.25)
# This part is for calculating the odds of safety, healing if you are safe, and how much treasure you get based on what door you choose
    if rounds > 1:
        print(f"Which door would you like to choose of 4? You have {rounds} floors of the dungeon left before you escape!")
    else:
        print("Which door would you like to choose of 4? This is your final floor to pick a door!")
    door = input("Door: ")
    if door == "1":
        safety_chance = 2
        healing_chance = 2
        treasure_value = 1
    elif door == "2":
        safety_chance = 2
        healing_chance = 2
        treasure_value = 2
        treasure_value += two_t_bonus
        safety_chance -= two_s_bonus
    elif door == "3":
        safety_chance = 3
        healing_chance = 3
        treasure_value = 3
        treasure_value += three_t_bonus
        safety_chance -= three_s_bonus
    elif door == "4":
        safety_chance = 4
        healing_chance = 4
        treasure_value = 4
        treasure_value += four_t_bonus
        safety_chance -= four_s_bonus
    else:
# This part is if someone inputs an invalid door
        print(f"The No Rule Breaking Goblin comes out of door {door} and kicks you out of the dungeon for picking his door!")
        quit()
    if safety_chance < 1:
        safety_chance = 1

    rounds -= 1
    safety = random.randint(1,safety_chance)
    healing = random.randint(1,healing_chance)
    time.sleep(.5)
# This part is checking if you are safe, and how much you heal if you get healing. If you do not get healing, then you will instead get treasure, which is calculated by adding the treasure bonus, then multiplying that by the treasure multiplier
    if safety == 1:
        print("You were safe!")
        if healing == 1:
            print(f"You healed {healing_bonus} health! Healthy!")
            health += healing_bonus
        else:
            treasure += treasure_value
            treasure *= treasure_multiplier
            print(f"You got {treasure_value} treasure! You now have {treasure} treasure!")
# This part happens if you are not safe, where a monster will make you lose 1 health    
    elif safety > 1:
        print(f"Uh oh! An evil monster cut you into {safety} slices!")
        print(f"You lost {monster_damage} Health!")
        health -= monster_damage
# If you run out of health, you lose the game and the program tells you how much treasure you lost with
        if health == 0 or health < 0:
            print(f"You're out of luck, and health! Bye bye, buddy!")
            if treasure > 20:
                time.sleep(.5)
                print(f"You lost with {treasure} treasure, that could have bought a good spatula!")
            else:
                print(f"You lost with {treasure} treasure! That couldn't have bought much, but it's still a shame!")
            quit()
    print(f"You have {health} health left!")
# This part is for storing the text that will appear for each reward slot depending on what reward you got
    reward_slot_1 = random.randint(1,8)
    if reward_slot_1 == 1:
        r1 = "1 - Boost Safety Chances on Door 2 by 1!"
    elif reward_slot_1 == 2:
        r1 = "1 - Boost Safety Chances on Door 3 by 1!"
    elif reward_slot_1 == 3:
        r1 = "1 - Boost Safety Chances on Door 4 by 1!"
    elif reward_slot_1 == 4:
        r1 = "1 - Boost Treasure Value on Door 2 by 1!"
    elif reward_slot_1 == 5:
        r1 = "1 - Boost Treasure Value on Door 3 by 1!"
    elif reward_slot_1 == 6:
        r1 = "1 - Boost Treasure Value on Door 4 by 1!"
    elif reward_slot_1 == 7:
        r1 = "1 - Boost all Healing by 1!"
    elif reward_slot_1 == 8:
        r1 = "1 - Multiply all Treasure found an additional time!"
    reward_slot_2 = random.randint(1,8)
    if reward_slot_2 == 1:
        r2 = "2 - Boost Safety Chances on Door 2 by 1!"
    elif reward_slot_2 == 2:
        r2 = "2 - Boost Safety Chances on Door 3 by 1!"
    elif reward_slot_2 == 3:
        r2 = "2 - Boost Safety Chances on Door 4 by 1!"
    elif reward_slot_2 == 4:
        r2 = "2 - Boost Treasure Value on Door 2 by 1!"
    elif reward_slot_2 == 5:
        r2 = "2 - Boost Treasure Value on Door 3 by 1!"
    elif reward_slot_2 == 6:
        r2 = "2 - Boost Treasure Value on Door 4 by 1!"
    elif reward_slot_2 == 7:
        r2 = "2 - Boost all Healing by 1!"
    elif reward_slot_2 == 8:
        r2 = "2 - Multiply all Treasure found an additional time!"
# This part is for assigning a reward to what option the user selects
    time.sleep(.5)
    print("Pick your reward!")
    print(f"{r1}")
    print(f"{r2}")
    choice = input("Choice: ")
    if choice == "1":
        if reward_slot_1 == 1:
            two_s_bonus += 1
        elif reward_slot_1 == 2:
            three_s_bonus += 2
        elif reward_slot_1 == 3:
            four_s_bonus += 1
        elif reward_slot_1 == 4:
            two_t_bonus += 1
        elif reward_slot_1 == 5:
            three_t_bonus += 1
        elif reward_slot_1 == 6:
            four_t_bonus += 1
        elif reward_slot_1 == 7:
            healing_bonus += 1
        elif reward_slot_1 == 8:
            treasure_multiplier += 1
    if choice == "2":
        if reward_slot_2 == 1:
           two_s_bonus += 1
        elif reward_slot_2 == 2:
            three_s_bonus += 2
        elif reward_slot_2 == 3:
            four_s_bonus += 1
        elif reward_slot_2 == 4:
            two_t_bonus += 1
        elif reward_slot_2 == 5:
            three_t_bonus += 1
        elif reward_slot_2 == 6:
            four_t_bonus += 1
        elif reward_slot_2 == 7:
            healing_bonus += 1
        elif reward_slot_2 == 8:
            treasure_multiplier += 1
# This part is for special events that happen at the end of each round
    event = random.randint(1,3)
    time.sleep(.25)
    if event == 1:
        print("A magic fairy flies through a hole in the wall.")
        print("Who might you be? Let us judge you, you see! Hee hee!")
        if health > 3:
            print("Seems you're doing well. Let's give thee a challenge, see!")
            monster_damage += 1
        else:
            print("Seems you may need a savior! May health be of you, my friend!")
            health += healing_bonus
    elif event == 2:
            print("A face peeks out of a strange hallway")
            print("Who might you be, young one? Spare three coins to a lonely old man?")
            if treasure > 2:
                print("Give 3 treasure to this old man?")
                print("1 - Give 3 Treasure")
                print("2 - Leave")
                choice == input("Choice: ")
                if choice == "1":
                    print("Why thank you, you're too kind! Here's something for your troubles.")
                    print("The old man boosts your safety in doors 2 and 3!")
                    three_s_bonus += 1
                    two_s_bonus += 1
                if choice == "2":
                    print("Pitiful little child! May you be cursed for 1000 years!")
                    print("The old man lowers your safety on door 2 by 1!")
                    two_s_bonus -= 1
            else:
                print("You don't have enough money, so you leave him to dwell in the shadows.")
    elif event == 3:
        print("At the bottom of a staircase you see a strange mushroom.")
        print("1 - Heal 4, but monsters deal 1 more damage")
        print("2 - Get 6 Treasure, but safety is lowered in doors 2-4")
        choice == input("Choice: ")
        if choice == "1":
            health += 4
            monster_damage += 1
        else:
            treasure += 6
            two_s_bonus -= 1
            three_s_bonus -= 1
            four_s_bonus -= 1
    elif event == 4:
        print("A brick wall covered in bugs stares at you with giant, creepy eyes.")
        print("Save us! Help us! Feed us!")
        print("1 - Lose 1 Health, +1 Healing Bonus")
        print("2 - +5 Treasure")
        choice == input("Choice: ")
        if choice == "1":
            if health == 1:
                healing_bonus += 1
            else:
                health -= 1
                healing_bonus += 1
        else:
            treasure += 5
    elif event == 5:
        print("A giant hand comes out of the ground and grabs your bag of treasure!")
        print("1 - Lose all treasure, +1 Safety on Door 4")
        print("2 - Lose 2 Health, double your Treasure")
        choice == input("Choice: ")
        if choice == 1:
            treasure = 0
            four_s_bonus += 1
        else:
            if health == 2:
                treasure *= 2
            else:
                health -= 2
                treasure *= 2
    elif event == 6:
        print("You hear a crying sound coming from the other room. After opening the door you see a baby with a big brain!")
        print("Hello, fellow intellectual. Might you wish you compare calculations?")
        print(f"1 - Set your health to 4 (Your current health is {health}!)")
        print(f"2 - Set your monster damage to 2 (Your current monster damage is {monster_damage}!)")
        choice == input("Choice: ")
        if choice == 1:
            health = 4
        else:
            monster_damage = 2

# This is what happens when you make it through all rounds
print(f"You made it to the end and escaped! You won with {health} health and {treasure} treasure!")