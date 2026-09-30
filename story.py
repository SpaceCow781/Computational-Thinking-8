place = input("You wake up. What place are you going to?")
print(f"Wow Brow. After a longy day at the {place}, you've run out of gas!")
print("Will you go to the Gas Station, or the Gas Emporium+?")
place2 = input()
if place2 == "gas station":
    print("You show up to the Gas Station, your car crying in hunger. Feed me please!")
    print("When you walk in, you see 3 isles. Which number isle would you like to go to?")
    isle = input()
    if isle == "1":
        print("As soon as you walk through, an old lady shows up. Fight Fight!")
        print("What are you gonna do? Hit or Fit?")
        fighting_old_ladies = input()
        print(f"You tried to land a {fighting_old_ladies}, but it didn't work!")
        print("Old Lady is level 3! She blocks your attack and sends you straight to jail! Locked away, okay!")
        print("Game Over!")
    elif isle == "2":
        print("You start going down aisle 2, and see a whole bunch of chips. Do you take some?")
        snacks = input()
        if snacks == "yes":
            print("You reach for the sustenance, but a little kid runs up and grabs it first! Monster!")
            print("Do you get on the chase or stay back and rest for warmth?")
            answer = input()
            if answer == "get on the chase":
                print("You get runnin' but the kid thought ahead and gets you in a trap!")
                print("Help help! He says! This guy's trying to take my snacks!")
                print("The police show up and send you straight to jail!")
                print("Game Over!")
            else:
                print("In the end you decided to stay back, but the fire you chose to start wasn't allowed!")
                print("Hey you! That's illegal! Straight to jail!")
                print("Game Over!")
        else:
            print("You pass on the snacks in the end, but the dude at the front who is behind the money trunk shouts at you!")
            print("I can't believe it. I offer you a building of treats and you accept none. None I tell ye'!")
            print("What is ye' namey, matey?")
            name = input()
            print(f"Well, {name}, I've ought to ban ye for breakin' the rules of the seven seas!")
            print("Arr is a consonant, not a vowel ye' see! So we better settle this like me mateys did when the kraken went straight for Billy's head!")
            print("A duel! 3 Knives on your side! No touching! You get tagged, you're out!")
            print("Do you accept his offer, or call the police?")
            answer = input()
            if answer == "accept his offer":
                print("He throws pounds of snacks at ya, each getting slashed by his seven swords!")
                print("It's ye-legal you see! Arrr! Straight to the brig to ya!")
                print("Game Over!")
            elif answer == "call the police":
                print(f"{name}, matey! I thought that we were mateys! Good thing I already didn't trust ye and called the police on the telly!")
                print("To jail!")
                print("Game Over!")
    elif isle == "3":
        print("As you start walking down the 3rd Isle you start to see some supplies. Yummy Yummy!")
        print("Do you buy some or leave?")
        answer = input()
        if answer == "buy some":
            print("Rude Rude Rude! The cashier at the front is yelling in all different directions!")
            print("Do you apologize or not? I don't have all day!")
            answer = input()
            if answer == "apologize":
                print("After you apologize they call you up to the front and have you buy all the stuff.")
                print("Unfortunately, you can't really afford this, so do you want to pay?")
                answer = input()
                if answer == "yes":
                    print("All of your bad spending left you debted! The bank shows up and sends you to kid jail!")
                    print("Game Over!")
                elif answer == "no":
                    print("Since you didn't pay for all of the stuff you took, the guy calls the cops and you get taken to jail")
                    print("Game Over")
            elif answer == "no":
                print("He pulls out some handcuffs and gets you! Secret Officer! Jail Time, Buddy!")
                print("Game Over!")
        elif answer == "leave":
            print("As you walk out the door you get attacked! Wow wow wow! The monsters run away and the police show up!")
            print("All those teeth on the ground, looks like you've commit crimes, friend. No thank you. To jail!")
            print("Game Over!")
elif place2 == "gas emporium":
    print("You see the gas emporium. All sorts of flavors are just behind those doors. But the gas guard shows up.")
    print("License and veggiestration please.")
    print("Do you lie or say your real name?")
    answer = input()
    if answer == "lie":
        print("You lie and say your name is something that isn't your name. Lies!")
        print("Sadly, the guard caught you in the act and you get arrested. To jail!")
        print("Game Over!")
    else:
        print("What's your name?")
        name = input()
        print(f"He let's you, {name} through, and you see two doors.")
        print("One door says 'cool pool' and the other says 'fool school'. Which doesn't drool, ghoul?")
        place3 = input()
        if place3 == "cool pool":
            print("You see a lemonade stand and a regular person standing next to it.")
            print("Do you take some lemonade or push the person?")
            answer = input()
            if answer == "push the person":
                print("You push that person into the pool! Pushin' club! Doo doo doo! Unfortunately, that wasn't showing kindness.")
                print("The guard from before, if you forgot, comes up and gets you! Now you're in jail.")
                print("Game over!")
            elif answer == "take some lemonade":
                print("You reach for the lemonade, but the person stops you.")
                print("Do you want to join the lemonade club? We've got 3 members. Me, my Pal, and my dog. But he's old, and won't last for long. Can't be transported.")
                print("But you could. I'll put you right into my waggon. Waggon lemonade club, like I said. Yes or no, pal?")
                answer = input()
                if answer == "yes":
                    print("The weirdo puts you in their waggon and drives away. Eventually he drinks too much lemonade and falls out of the waggon.")
                    print("You take the wheel, and it flies off! You crash into a wall, and the cops send you to jail for crimes!")
                    print("Game Over!")
                elif answer == "no":
                    print("Guards! Get this denier. They were mean to me.")
                    print("The guards surround you as the weird dude goes into the bushes that were there the whole time. You get sent to pool jail!")
                    print("Game over!")
        else:
            print("Do you want to go to class or skip it?")
            answer = input()
            if answer == "go to class":
                print("Once you get to class, the teacher closes the door and everyone jumps into their seats.")
                print("You misbehavers! I've ought to send each and every one of you to jail!")
                print("This is exactly why I'm gonna teach ya how to be a police officer. If you see anything out of line, send 'em to jail! Right away!")
                print("As you fall asleep in your seat, you see all the ways you will help/hurt others as a police officer.")
                print(f"You wonder if this would have even happened if you didn't go to the {place} all along.")
                print("You won!")
            else:
                print("You decide to wander the halls. Uh oh! It's the head of school! And they are very mad mad mad!")
                print("You rotten child! Evil Queen!")
                print("The principal picks up your hair and starts swinging you around!")
                print("You get thrown out through the window and into the closest jail.")
                print("Game Over!")