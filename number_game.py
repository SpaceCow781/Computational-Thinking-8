import random

hidden_number = random.randint(1,7)
month = "January"

# print(hidden_number)
# to loop something do: for i in range(put loop value here):
my_birthday = int(input("Guess a number 1-7: "))

for i in range(2):
    if my_birthday == hidden_number:
        print(f"That's my birthday! {month} {hidden_number}!")
        quit()
    else:
        if my_birthday > hidden_number:
            print("That's my birthday! Not! My birthday is a lower number!")
        else:
            print("That's my birthday! Not! My birthday is a higher number!")
else:
    print(f"You lose! My birthday was {month} {hidden_number}!")