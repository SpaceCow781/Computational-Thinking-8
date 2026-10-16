t_t = 0
t_g = 0
d = 0
s = 0
j = 0
p = 0
b = 0
q = 0
f = 0
e = 0

print("Do you want to learn where you should live?")
print("")
print("Type the number 1 for the first option: Yes!")
print("")
print("Type the number 2 for the second option: No!")
print("")
print("This will go on chronologically for any additional options!")
answer = input("Answer: ")
if answer == "2":
    print("Ok then, I guess we don't have to if you don't want to.")
    quit()
else:
    print("Let's continue!")
print("Time for question 1! What is your favorite color?")
print("")
print("Red, Orange, Yellow, Green, Blue, or Purple?")
answer = input("Favorite Color: ")
if answer == "1":
    j += 1
    b += 1
elif answer == "2":
    d += 1
    q += 1
elif answer == "3":
    t_g += 1
    f += 1
elif answer == "4":
    p += 1
    e += 1
elif answer == "5":
    t_t += 1
else:
    s += 1
print("Time for question 2! Do you like nature, buildings, or water?")
answer = input("Answer: ")
if answer == "1":
    t_g += 2
    d += 1
    b += 1
elif answer == "2":
    t_t += 2
    s += 1
    q += 1
else:
    j += 1
    p += 1
    f += 1
    e += 1

print("Don't you see it's question three! Do you like Cloudy, Sunny, Rainy, or Rural weather?")
answer = input("Answer: ")
if answer == "1":
    t_t += 1
    p += 1
    q += 1
    e += 2
elif answer == "2":
    t_g += 1
    d += 1
    b += 2
elif answer == "3":
    j += 1
    d += 2
    f += 1
    t_t += 1
else:
    p += 2
print("Time for more it's question four! Is your favorite food Purple Pig or Frail Snails?")
answer = input("Answer: ")
if answer == "1":
    d += 2
    t_t += 1
    s += 1
    q += 1
else:
    j += 1
    e += 1
    f += 1
    p += 1
    t_g += 1
print("Don't break out in hives it's question five! What board game do you like the most? Secret Thursday, Snake Finder 63, or Lemon Theory?")
answer = input("Answer: ")
if answer == "1":
    t_t += 1
    j += 1
    f += 1
    b += 2
elif answer == "2":
    t_g += 1
    d += 1
    q += 1
else:
    p += 1
    e += 1
    s += 2
print("Building Bricks it's question six! Who do you fear: Old Man Chilly, or the Ghost of the Ocean?")
answer = input("Answer: ")
if answer == "1":
    d += 2
    j += 2
    b += 1
    t_g += 1
    f += 1
else:
    t_t += 1
    s += 1
    p += 1
    q += 1
    e += 1
print("Don't tell Kevin it's question seven! Where do you live already?")
print("The secret special options are: New Florida, The East Pole, Cardboard Castles, Windy Wonders, Mint Mountain, or Greater Than or Equal to Planet?")
answer = input("Answer: ")
if answer == "1":
    t_g += 1
    e += 1
elif answer == "2":
    d += 1
elif answer == "3":
    t_t += 1
    b += 2
elif answer == "4":
    j += 1
    f += 2
elif answer == "5":
    p += 1
    q += 1
else:
    s += 1
print("You're not doing great it's question eight! What's your opinion on Endangered Species? Do you like them or hate them?")
answer = input("Opinion: ")
if answer == "1":
    j += 1
    d += 1
    q += 1
    f += 1
    t_g += 1
else:
    t_t += 2
    p += 1
    b += 1
    e += 1
    s += 3
print("Number line it's question nine! Did you Bring Today's Best? Yes or No? ")
answer = input("Answer: ")
if answer == "1":
    p += 1
    j += 1
    f += 1
    t_t += 1
    e += 1
else:
    d += 1
    b += 1
    q += 2
    t_g += 1
    s += 1
print("Come again it's question ten! What is your name?")
name = input("Type Here in all Lowercase: ")
if name[0] == "a" or name[0] == "e" or name[0] == "i" or name[0] == "o" or name[0] == "u":
    d += 1
    t_g += 2
    f += 1
    e += 2
    j += 1
else:
    t_t += 1
    p += 1
    q += 1
    b += 1
    s += 1

# This is the ending for Tooth Town - You get this by getting the most t_t points
if t_t > t_g and t_t > d and t_t > j and t_t > s and t_t > p and t_t > b and t_t > q and t_t > f and t_t > e:
    print("You should absolutely live in Tooth Town! HAGS!")
    quit()
# This is the ending for the Deer Sphere - You get this by getting the most d points
elif d > t_t and d > t_g and d > j and d > s and d > p and d > b and d > q and d > f and d > e:
    print("You should absolutely live in the Deer Sphere! Don't go toward the Moths!")
    quit()
# This is the ending for the Tiptoe Gardens - You get this by getting the most t_g points
elif t_g > d and t_g > t_t and t_g > j and t_g > s and t_g > p and t_g > b and t_g > q and t_g > f and t_g > e:
    print("You should absolutely live in the Tiptoe Gardens. Do not fear!")
    quit()
# This is the ending for Josh Hall - You get this by getting the most j points
elif j > t_g and j > t_t and j > d and j > s and j > p and j > b and j > q and j > f and j > e:
    print("You should absolutely live in Josh Hall! Happy Birthday!")
    quit()
# This is the ending for Shrill Village - You get this by getting the most s points
elif s > t_g and s > t_t and s > j and s > d and s > p and s > b and s > q and s > f and s > e:
    print("You should absolutely live in Shrill Village! Who's in your Will?")
    quit()
# This is the ending for Baby Beach (Kids) - You get this by getting the most b points
elif b > t_g and b > t_t and b > j and b > d and b > p and b > s and b > q and b > f and b > e:
    print("You should absolutely live at Baby Beach (Kids)! Time to grow up!")
    quit()
# This is the ending for Quail Quarry - You get this by getting the most q points
elif q > t_g and q > t_t and q > j and q > d and q > p and q > s and q > b and q > f and q > e:
    print("You should absolutely live at Quail Quarry! Be Mindful!")
    quit()
# This is the ending for Frosty England - You get this by getting the most f points
elif f > t_g and f > t_t and f > j and f > d and f > p and f > s and f > b and f > q and f > e:
    print("You should absolutely live in Frosty England! Hire a Haberdasher, and quick!")
    quit()
# This is the ending for Evil Inventions Senior Center - You get this by getting the most e points
elif e > t_g and e > t_t and e > j and e > d and e > p and e > s and e > b and e > q and e > f:
    print("You should absolutely live in Evil Inventions Senior Center! Say hi to Grandpa!")
    quit()
# This is the ending for Picklepoint+ - You get this by getting the most p points
elif p > t_g and p > t_t and p > j and p > d and p > e and p > s and p > b and p > q and p > f:
    print("You should absolutely live in Picklepoint+! Eat your vegetables (and fruits)!")
    quit()
# This is the ending for Normal Neighborhood - This is only achieved in a case where somehow all the point checking statements before are false
else:
    print("You should absolutely live in the Normal Neighborhood! No Ghosts Here!")