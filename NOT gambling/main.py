import random
import os

score = 0
totalBalance = 100


def game(a):
    
    
    clear = lambda: os.system('cls')

    global score
    global totalBalance
    bet = 0

    if totalBalance <= -1000:
        print("SCORE:", score)
        print()
        print("BALANCE:", totalBalance)
        print()
        print(
            "Regrettably, you are completely broke. As such, we cannot allow you to continue playing."
        )
        print()
        print("Our sincerest regrets!")
        print()
        print("   - The Gambler's Assn.")
        exit()

    card1 = random.randint(1, 10)
    card2 = random.randint(1, 10)
    card3 = random.randint(1, 10)

    print("SCORE:", score)
    print()
    print("BALANCE:", totalBalance)
    print()
    print("[ 1 ]  [ 2 ]  [ 3 ]")

    print()

    #choose [1/2/3]
    while True:
        try:
            chosen = int(input("Choose a card: "))
            if 0 <= chosen <= 3:
                break
            raise Exception()
        except:
            clear()
            print("SCORE:", score)
            print()
            print("BALANCE:", totalBalance)
            print()
            print("[ 1 ]  [ 2 ]  [ 3 ]")
            print()
            print("Please enter 1, 2, or 3!")
            print()

    print()
    print("You chose card", chosen, "!")
    print()
    print("Are you sure you want to choose this card?")
    print()

    #ok but are you sure
    while True:
        try:
            confirm = str(input("[Y/N] "))
            if confirm.upper() in ("Y", "YES", "YE", "N", "NO", "NOPE"):
                break
            raise Exception()
        except:
            clear()
            print("SCORE:", score)
            print()
            print("BALANCE:", totalBalance)
            print()
            print("[ 1 ]  [ 2 ]  [ 3 ]")
            print()
            print("You chose card", chosen, "!")
            print()
            print("Please input 'Y' or 'N'!")
            print()
            print("Are you sure you want to choose this card?")
            print()

    #no? okay
    while confirm.upper() == "N":
        while True:
            try:
                clear()
                print("SCORE:", score)
                print()
                print("BALANCE:", totalBalance)
                print()
                print("[ 1 ]  [ 2 ]  [ 3 ]")
                print()
                chosen = int(input("Choose a card: "))
                if 0 <= chosen <= 3:
                    break
                raise Exception()
            except:
                clear()
                print("SCORE:", score)
                print()
                print("BALANCE:", totalBalance)
                print()
                print("[ 1 ]  [ 2 ]  [ 3 ]")
                print()
        print()
        print("You chose card", chosen, "!")
        print()
        print("Are you sure you want to choose this card?")
        print()
        while True:
            try:
                confirm = str(input("[Y/N] "))
                if confirm.upper() in ("Y", "YES", "YE", "N", "NO", "NOPE"):
                    break
                raise Exception()
            except:
                clear()
                print("SCORE:", score)
                print()
                print("BALANCE:", totalBalance)
                print()
                print("[ 1 ]  [ 2 ]  [ 3 ]")
                print()
                print("You chose card", chosen, "!")
                print()
                print("Please input 'Y' or 'N'!")
                print()
                print("Are you sure you want to choose this card?")
                print()

    #make a bet?
    flag = 0
    while flag == 0:
        clear()
        print("SCORE:", score)
        print()
        print("BALANCE:", totalBalance)
        print()
        print("[ 1 ]  [ 2 ]  [ 3 ]")
        print()
        print("Your card is:", chosen)
        print()
        doBet = input("Do you want to make a bet? [Y/N] ")
        if doBet.upper() in ("Y", "YES", "YE"):
            while flag == 0:
                print()
                bet = int(input("How much do you bet? "))
                if bet >= 1:
                    flag = 1
                elif bet <= 0:
                    clear()
                    print("SCORE:", score)
                    print()
                    print("BALANCE:", totalBalance)
                    print()
                    print("[ 1 ]  [ 2 ]  [ 3 ]")
                    print()
                    print("Your card is:", chosen)
                    print()
                    print("Enter a positive integer!")
                    print()
                    bet = int(input("How much do you bet? "))
        else:
            flag = 1

    clear()
    print("SCORE:", score)
    print()
    print("[", card1, "]", "[", card2, "]", "[", card3, "]")
    print()

    #determining other values
    if chosen == 1:
        chval = card1
        ot = card2
        her = card3
    elif chosen == 2:
        chval = card2
        ot = card1
        her = card3
    elif chosen == 3:
        chval = card3
        ot = card2
        her = card1

    #win condition
    if chval >= ot and chval >= her:
        clear()
        score += 1
        totalBalance = totalBalance + bet
        print("SCORE:", score)
        print()
        print("BALANCE:", totalBalance)
        print()
        print("[", card1, "]", "[", card2, "]", "[", card3, "]")
        print()
        print("You win!")

    else:
        clear()
        totalBalance = totalBalance - bet
        print("SCORE:", score)
        print()
        print("BALANCE:", totalBalance)
        print()
        print("[", card1, "]", "[", card2, "]", "[", card3, "]")
        print()
        print("You lose.")
    return ("")


def main():
    global score
    global totalBalance
    clear = lambda: os.system('cls')

    print('RULES:')
    print()
    print("There are three cards, and each card has a certain value. You must pick a card, and if your card's value is the highest, you win!")
    print()
    print("You may also place a bet. If you win, your bet gets added to your total balance, but if you lose, it gets subtracted from your total balance.")
    print()
    print("If your balance falls below -1000, you cannot continue playing, so bet responsibly!")
    print()
    input("Enter any key to continue. ")
    clear()
    print(game(0))
    while True:
        print()
        print("Replay?")
        print()
        play_again = input('[Y/N] ')

        if play_again.lower() not in ("y", "yes", "ye", ""):
            quit()
        else:
            clear()
            game(0)


main()