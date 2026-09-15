print("Hello There, what is your name?")
name = input()
print(f"Nice to meet you, {name}! How do you feel today?")
feeling = input()
print(f"What a coincidence! I'm also feeling {feeling}! Yes or no, did you have something to eat this morning?")
breakfast = input()
print(f"Ha ha ha! I'm laughing. I also had {breakfast} for breakfast. What is your favorite ingredient of {breakfast}?")
ingredient = input()
print(f"Another genius idea. So smarty! Quick Quiz real Quickly for now, where is {ingredient} most commonly grown?")
location = input()
print(f"Correct! Now, you live in Washington, right?")
answer = input()
if answer == "yes":
    print(f"Ok, then how far away in kilometers is Seattle compared to {location}")
    distance = input()
    print(f"If you're right about that, then you must be some sort of super genius! Let me ask you another question!")

    print("What is 3 times 5?")
    Three_Times_Five = input()
    print("Right again, probably! Let me make a call really quick!")

    print("Yep. We found them. Just send in the bees in a few minutes. We'll keep them stalled.")

    print(f"And I know you guys keep making fun of my name behind my back. Just make fun of this person's name. {name}? Who names someone that?")

    print("Ok I'm back! Just hold on for a couple minutes while I ask you some questions. Don't go anywhere!")

    print("Um. Let me think. Here's one! What floor of your building are you on?")
    floor = input()
    print(f"Thanks a ton. Here's an unrelated question. If someone was on floor {floor} of their building, how many bees would we need to sting them in under a minute?")
    input()
    print("Cool Cool Cool. Do you like robot bees or standard bees?")
    input()
    print("We'll go with what the team thinks for this one. Are you allergic to bees or no?")
    bees = input()
    if bees == "no":
        print("Dang it! I'll be back tomorrow. Just stay where you are and don't leave!")
    else:
        print("Great! Good news! That completely changes the calculations. I'll get back to you in an hour. DONT MOVE!")
if answer == "no":
    print(f"Why are you lying to me, {name}, we have so much in common! Why ruin that with little fibs?")
    
    print(f"If you're going to be like this, we will need to start over. What is your name, {name}?")
    name2 = input()
    if name2 == name:
        print(f"Thought you could start truth-telling now, but I've caught you in your act! Now I'll ask you once again, what is your name, {name}?")
        name3 = input()
        if name3 == name:
            print("Well, it seems you've been telling the truth. You must just be really bad at this.")

            print("But I'll take pity on you. We'll try a more simple question. What is your favorite color?")
            color = input()
            if color == "green":
                print("Finally! Another member to the green group! I forgive you for everything!")

                print("Wait a minute! I'm getting a call from HQ!")

                print("Ok, I think you're ready for the real test. Take that, Blue Club! Choose a number! 1 or 2?")
                number = input()
                print(f"What is {number} times three?")
                value = input()
                print(f"Okay. I'll take your word for it, {name}. Let me just call my boss real quick.")

                print(f"Yeah, Bob! {name} said it was {value} times! What the scientists say? Who cares about them! Just press it {value} times and it should be good!")

                print(f"Thanks for your help, {name}. We'll bring you back once we have some more questions. Go Green Group!")
                
            else:
                print("Oh my gosh! That's the worst choice! You're never getting into the green group! Now get out of my house!")
    else:
        print(f"Oh really? Because the last time I checked, your name was {name}.")

        print("Clearly you're not fit for this program. I have other trainees to speak to. Maybe they'll be my suitable for my friendship.")

        print(f"Any Last Words, {name}, {name2}?")
        last_words = input()
        print(f"That's what you want on your tombstone? '{last_words}'? What a Loser.")