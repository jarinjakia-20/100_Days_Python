import random
import My_module

random_integer = random.randint(1,10)
print(random_integer)

print(My_module.my_favourite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)