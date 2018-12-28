'''
world1 = []
world2 = []
world = []
result = " "
print('Initial Count: ' + result)

def print_world1(world1):
    for x in range(3):
        world1= (["O"] * 11)
        print (" ".join(world1))
    return world1

def print_world2(world2):
    for x in range(5):
        world2= (["X"] * 11)
        print (" ".join(world2))
    return world2

world = print_world1(world1) + print_world2(world2)

print(world)


for x in range(0, 10):
    if world1[x]== "X":
        print_world1(world1[x][y])
    result = result + print_world1(world1[x])

print('The total number of continents is: ' + result + 'First Hackathon Complete. Thank you!!')
'''
import random

option = ['o', 'o', 'o', 'o', 'o', 'o', 'x']
land = []
number = 0
count = 0
while count != 11:
    for i in range(11):
        random.shuffle(option)
        land.append(option[0])
        if option[0] == 'x':
            number +=1


    print(' '.join(land))
    land.clear()
    count += 1

number = str(number)

print('The total number of continents is: ' + number + ' First Hackathon Complete. Thank you!!')
