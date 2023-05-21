print('Welcome to my space quiz :)')

user_playing = input('Do you want to play? ')

if user_playing.lower() != 'yes':
    quit()

print("Okay yay let's play my space quiz!")
score = 0

answer = input("Which planet is covered by clouds of sulphuric acid? ")
if answer.lower() == 'venus':
    print('Correct!!')
    score += 1
else: print('Incorrect')

answer = input("Which planet is closest to the sun? ")
if answer.lower() == 'mercury':
    print('Correct!!')
    score += 1

else: print('Incorrect')

answer = input("Which is the largest planet in the solar system? ")
if answer.lower() == 'jupiter':
    print('Correct!!')
    score += 1

else: print('Incorrect')

answer = input("Which planet has a day which lasts eight months? ")
if answer.lower() == 'venus':
    print('Correct!!')
    score += 1
else: print('Incorrect')

answer = input("Which planet takes almost 30 Earth years to orbit the sun? ")
if answer.lower() == 'saturn':
    print('Correct!!')
    score += 1
else: print('Incorrect')


print('You got ' + str(score) + ' (' + str((score / 5) * 100) + '%) ' + 'questions correct!')
