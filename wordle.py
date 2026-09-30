import random

# Pick a word at random
word_list = ["heart","loopy","goopy","audio","laugh","trial","mango","sandy","fears","tears","child","green","ropes","round","sound","mound"]
hidden_word = random.choice(word_list)


# Guess a word
print(f"Guess your word, kid! It's totally not {hidden_word}!")
guess_word = input()
output = ""

# First letter (in python, counting starts at 0 not 1)
if guess_word[0] == hidden_word[0]:
    output += "🟩"
elif guess_word[0] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# 2
if guess_word[1] == hidden_word[1]:
    output += "🟩"
elif guess_word[1] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# 3
if guess_word[2] == hidden_word[2]:
    output += "🟩"
elif guess_word[2] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# 4
if guess_word[3] == hidden_word[3]:
    output += "🟩"
elif guess_word[3] in hidden_word:
    output += "🟨"
else:
    output += "⬛"

# 5
if guess_word[4] == hidden_word[4]:
    output += "🟩"
elif guess_word[4] in hidden_word:
    output += "🟨"
else:
    output += "⬛"


# Result
print(output)
if output == "🟩🟩🟩🟩🟩":
    print("You win")
if output != "🟩🟩🟩🟩🟩":

        # 2nd Try
    print(f"Try again! Just to clarify, the answer isn't {hidden_word}!")
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # 2
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # 3
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # 4
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # 5
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Result
print(output)
if output == "🟩🟩🟩🟩🟩":
    print("You win")
if output != "🟩🟩🟩🟩🟩":

    # 3nd Try
        print(f"Last try! And for the final time, the guess isn't {hidden_word}!")
        guess_word = input()
        output = ""

        # First letter (in python, counting starts at 0 not 1)
        if guess_word[0] == hidden_word[0]:
            output += "🟩"
        elif guess_word[0] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # 2
        if guess_word[1] == hidden_word[1]:
            output += "🟩"
        elif guess_word[1] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # 3
        if guess_word[2] == hidden_word[2]:
            output += "🟩"
        elif guess_word[2] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # 4
        if guess_word[3] == hidden_word[3]:
            output += "🟩"
        elif guess_word[3] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"

        # 5
        if guess_word[4] == hidden_word[4]:
            output += "🟩"
        elif guess_word[4] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"
                    # Result
        print(output)
        if output == "🟩🟩🟩🟩🟩":
            print("You win")
        if output != "🟩🟩🟩🟩🟩":
            print(f"You lost! The answer was {hidden_word}!")
            quit()