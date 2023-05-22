name = input('What is your name: ')
print("Welcome", name, "to this space adventure")
answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left':
    q2 = input("You come across a wormhole, and you can enter it or explore the surrounding area. Type 'enter' to go through the wormhole or 'explore' to investigate the surroundings: ").lower()

    if q2 == 'enter':
        print('You bravely entered the wormhole and found yourself in a distant galaxy')
    elif q2 == 'explore':
        print("You explored the area and discovered a hidden space outpost")
    else:
        print('Not a valid option')

elif answer == 'right':
    q2 = input("You come across a lunar base, and you can join the astronauts on a mission or continue your journey alone. Type 'join' to accompany the astronauts or 'continue' to walk on: ").lower()

    if q2 == 'join':
        print('You joined the astronauts and embarked on an incredible space adventure')
    elif q2 == 'continue':
        print("You decided to continue your journey, traversing the vast expanse of space")
    else:
        print('Not a valid option')

else:
    print("Not a valid option")
