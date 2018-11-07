import random


def dice_roll():
    while True:
        print("Your number is: " + str(random.randint(1, 6)))
        play_again = input("Would you like to play again [y/n]?")
        while play_again != 'y':
            if play_again == 'n':
                return print("Game Over Goodbye!")
            else:
                print("Input not recognized!!!")
                play_again = input("Would you like to play again? ")


def main(data):
    game_start = data
    if (game_start == 'y'):
        dice_roll()
    elif(game_start == 'n'):
        return 'Game over Goodbye!'
    elif(game_start != 'n' or game_start != 'y'):
        return 'Not recognised!'


def input_data():
    data = input("Would you like to roll the dice [y/n]?")

    if data == '':
        main(data)
    else:
        "No data Submitted"


if __name__ == '__main__':
    main()
