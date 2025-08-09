#Who will pay the bill ? Choose a random name using List and Random
import random 

friends = ["Anni", "Mim", "Nadia", "Rupa", "Taposhi"]
# 1st procedure
print(random.choice(friends))

#2nd procedure
random_index = random.randint(0, 4)

print(friends[random_index])