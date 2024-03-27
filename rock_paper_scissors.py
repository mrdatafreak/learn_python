import random

computer_score = 0
human_score = 0
number_of_ties = 0
keep_playing = True

while keep_playing:
    # Computer makes its choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # print('The computer chooses ' + computer_choice)

    # Human makes their choice
    human_choice = input('Enter human choice (rock, paper, scissors): ')
    print('Human chooses ' + human_choice)

    # Determine the outcome of the round
    if human_choice == computer_choice:
        number_of_ties += 1
        print('Tie')
    elif ((human_choice == 'rock' and computer_choice == 'paper') or
          (human_choice == 'paper' and computer_choice == 'scissors') or
          (human_choice == 'scissors' and computer_choice == 'rock')):
        computer_score += 1
        print('Computer wins')
    else:
        human_score += 1
        print('Human wins')

    # Ask if the player wants to continue
    print("Do you want to play again? (yes/no)")
    answer = input()
    if answer.lower() != "yes":
        keep_playing = False
        print("Thanks for playing!")
        print('Computer score: ' + str(computer_score))
        print('Human score: ' + str(human_score))
        print('Ties: ' + str(number_of_ties))
