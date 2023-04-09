"""Create your own adventure: Would you survive?"""

__author__ = 730554082

# import library
import random

# globals
points: int = 0
player: str = ""

# random
carrots: int = random.randint(3, 10)
random_number: int = random.randint(1, 10)

# constants
SMILE_EMOJI = "\U0001F604"	
STAR_EMOJI = "\U00002B50"
GREEN_CHECK = "\U00002705"
RED_CROSS = "\U0000274C"
FORK_KNIFE = "\U0001F374"


def greet() -> None:
    """Introduces game to the player."""
    # Print welcome message
    print(f"Want to find out if you can survive in the notoriously rude and terrifing chef, Gordon Ramsay's kitchen? {FORK_KNIFE}\nPlay this adventure game to find out!")

    # Get player's name
    global player
    name = str(input("\nLet's start! What's your name? "))
    player = name.capitalize()


def conclude(conclusion: int) -> None:
    """Picks the ending for the game."""
    if conclusion == 1:
        print(f"\nCongratulations {player}, it looks like you survived Gordon Ramsay's misery. {SMILE_EMOJI}\nYou earned a total of {points} points. Looks like there's potential to be a future michelin star {STAR_EMOJI}")
    elif conclusion == 2:
        print(f"\nWell that was a fun journey {player}, but looks like you weren't able to survive. 'Hell's Kitchen' was named for a reason {SMILE_EMOJI}. \nYou did manage to get {points} points, good job!")
    elif conclusion == 3:
        print(f"\nYOU NAILED IT {player.upper()}! You passed every single challenge and now you and Gordon are absolute besties {SMILE_EMOJI}! You're basically a michelin star chef {STAR_EMOJI}. \nYou're total points were {points}.")
    return conclusion


def bonus(current: int) -> int:
    """Gives bonus points to player."""
    guess = int(input(f"\n {player}, to get bonus points, guess a number from 1 to 10"))
    global random_number
    if guess == random_number:
        current += guess
        print(f"Woah {player}! You got {guess} more points. Now you're total is {current}")
    else:
        print(f"Bad luck {player}, you didn't get any extra points.")
    return current


def choice1() -> None:
    """If the player lied about why they were late."""
    # Access globals
    global points 
    points += 10
    print(f"\nA white lie isn't always harmful, good decision.The kitchen is running late today so Gordon wants you to help out in prepping things, he asks you to julienne {carrots} carrots. How would you cut the carrots?")
    decision = int(input("\n1: You cut small, 1-inch cubes. \n2: You cut 2-inch thin strips. "))
    if decision == 2:
        points += 10
        print(F"\nAmazing {player}! {GREEN_CHECK} Now that Gordon trusts you, he wants you to set the table for our guests, which order does the cutlery go in?")
        decision_1 = int(input("\n1: Spoons and Forks on the left amd Knives on the right. \n2: Forks on the left and knives and spoons on the right "))
        if decision_1 == 2:
            points += 10
            print(f"\nPerfect {player}, what a genius !{GREEN_CHECK} Now you have to help in making a souffle, what temperature should we set the oven to? ")
            decision_2 = int(input("\n1: 400 Farenheit. \n2: 250 Farenheit. "))
            if decision_2 == 1:
                points += 10
                print(f"\nWoah {player}! Absolute machine. {GREEN_CHECK} Gordon sees the potential in you, so he jokes around and asks you to grab a spice, but all he says is 'Grab the expensive stuff {SMILE_EMOJI}'. What are you grabbing?")
                decision_3 = int(input("\n1: Fennel Seeds. \n2: Saffron"))
                if decision_3 == 2:
                    points += 10
                    print(f"\nYou really know your stuff {player}! {GREEN_CHECK} Now it's getting really serious, you've been asked to be at the pass. Where are you going?")
                    decision_4 = int(input("\n1: The table from where the plates are taken by the waitstaff. \n2: The area between the cooking station and the cleaning station. "))
                    if decision_4 == 1:
                        points += 10
                        print(f"\nPhew, you made it to the right spot! {GREEN_CHECK} Looks like you're at the last test. Gordon asks you to grab a glass of wine to open together, which bottle do you grab?")
                        decision_5 = int(input("\n1: Wine made in an Oak Barrel from an difficult to manage climate. \n2: Wine made in a Pine Barrel from a rich and healthy climate. "))
                        if decision_5 == 1:
                            points += 10
                            print(f"\nYES! YOU MADE IT. {GREEN_CHECK}")
                            conclude(3)
                        else:
                            points -= 5
                            print(f"\nSHOOT! You did {player}, amazing but unfortunatley, this was wrong. {RED_CROSS}")
                            conclude(1)
                    else:
                        points -= 5
                        print 
                        conclude(1)
                else:
                    points -= 5
                    print(f"\nThat one was hard {player}, but fennel seeds aren't the right answer. {RED_CROSS}")
                    conclude(1)
            else:
                points += 10
                print(f"\nOh no {player}! You were doing so well but looks like you're serving souffle soup here. {RED_CROSS}")
                conclude(2)
        else: 
            points -= 5
            print(f"\nLooks like you got the arrangement wrong! {RED_CROSS}")
            conclude(2)
    else:
        points -= 5
        print(f"\nOops, looks like you've wasted {carrots} carrots. {RED_CROSS}")
        conclude(2)


def choice2() -> None:
    """If the player was honest about why they were late."""
    # Access globals
    global points 
    points += 5
    print("\nHonesty is always the best policy, but thankfully Gordon's in a good mood today. He's running a little behind so he asks you to rock chop some cilantro, how do you do that? ")
    decision = int(input("\n1: You cut roughly chop it into large chunks. \n2: You rock your knife back and forth and mince it."))
    if decision == 2:
        points += 10
        print(f"\nAmazing {player}! {GREEN_CHECK} Now that Gordon trusts you, he wants you to help in setting the table, how are the glasses arranged?")
        decision_1 = int(input("\n1: Water glass on the outside and Wineglass on the inside \n2: Wineglass on the outsdie and Water glass on the inside."))
        if decision_1 == 2:
            points += 10
            print(f"\nPerfect {player}, what a genius!{GREEN_CHECK} Now you have to help in setting up a double boiler. How do you do that?")
            decision_2 = int(input("\n1: Set up a pot with some water and a metal bowl on top.\n2: Set up two pots, one salted water and another without salt."))
            if decision_2 == 1:
                points += 10
                print(f"\nWoah {player}! Absolute machine. {GREEN_CHECK} Gordon sees the potential in you, so he jokes around and asks you to grab you some honey, but all he says is 'Grab the stuff Kiwis love {SMILE_EMOJI}'. What are you grabbing?")
                decision_3 = int(input("1: Alfalfa Honey\n2: Manuka Honey."))
                if decision_3 == 2:
                    points += 10
                    print(f"\nYou really know your stuff {player}! {GREEN_CHECK} Now it's getting really serious, you've been asked to grab some milk out of the low boy. Where are you reaching for the milk?")
                    decision_4 = int(input("\n1: The undercounter refrigerator. \n2: The area between the cooking station and the cleaning station."))
                    if decision_4 == 1:
                        points += 10
                        print(f"\nPhew {player}, you made it to the right spot! {GREEN_CHECK} Looks like you're at the last test. Gordon asks you to grab some 'spumante', which bottle do you grab?")
                        decision_5 = int(input("\n1: A Bottle of expensive Champagne from Italy. 2: A Wine Bottle from the vineyards in Greece. "))
                        if decision_5 == 1:
                            points += 10
                            print(f"\nYES! YOU MADE IT. {GREEN_CHECK}")
                            conclude(3)
                        else:
                            points -= 5
                            print(f"\nSHOOT! You did amazing but unfortunatley, this was wrong. {RED_CROSS}")
                            conclude(1)
                    else:
                        points -= 5
                        print 
                        conclude(1)
                else:
                    points -= 5
                    print(f"\nThat one was hard {player}, but Alfalfa honey isn't the right answer. {RED_CROSS}")
                    conclude(1)
            else:
                points += 10
                print(f"\nOh no {player}! You were doing so well but looks like you're diluting chocolate here. {RED_CROSS}")
                conclude(2)
        else: 
            points -= 5
            print(f"\nLooks like you got the arrangement wrong! {RED_CROSS}")
            conclude(2)
    else:
        points -= 5
        print(f"\nOops, looks like you've wasted {carrots} carrots. {RED_CROSS}")
        conclude(2)


def main() -> None:
    """Runs the main loop of the game."""
    run_game = "Y"
    high_score = 0
    greet()
    while run_game.upper() == "Y":
        # Introduce main challenge with 3 choices:
        print("\nAs a struggling chef in NYC, you were invited to spend a day at Gordon Ramsay's kicten. He send you an email with just the venue, time and his signature. Unfortunately, you overslept and you enter the restaurant 10 minutes later than you were supposed to.")

        main_decision = int(input(f"{player}, you know first impressions matter the most, how do you proceed here. Enter the number for your choice: \n 1:Decide to lie and say that you got stuck helping an old woman cross the street. \n 2: Be honest and tell him that you accidentally overslept. \n 3: You decide to cut your losses and immediately turn around and leave the kitchen."))

        if main_decision == 1:
            choice1()
        elif main_decision == 2:
            choice2()
        else: 
            print("\nSometimes, it makes sense to escape a bad situation, who would want to deal with that mess?")
            global points
            points += 5
            conclude(1)
        
        if points > high_score:
            high_score = points

        points = bonus(points)
        
        print(f"{player} your high score is {high_score} and you current score is {points}.")
        run_game = str(input(f"\nDo you want to play again {player}? Enter 'Y' or 'N'"))

        points = 0


if __name__ == "__main__":
    main()
