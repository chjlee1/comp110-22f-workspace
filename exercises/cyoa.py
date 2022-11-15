"""EX06 - Choose Your Own Adventure; Farming Game!"""

__author__: str = "730571111"

from random import randint

player: str = ""
points: int = 0
multiplier: float = 1.0
rate: int = 20
secret: bool = False

SHINE: str = "\u2728"
CORN: str = "\U0001f33d"
WHEAT: str = "\U0001F33E"
EGGPLANT: str = "\U0001F346"


def greet() -> None:
    """Greets the player and gives a brief explanation of game."""
    global player
    print("------\nHello! Welcome to the most basic Farming Game you'll ever play!")
    print("Your job is to grow crops and earn points. You can use your points to buy new upgrades!\n------")
    print("You're the main protagonist, so you're going to need a name!")
    player = input("What is your name?\n")


def farm() -> None:
    """Player can choose which crop to grow. Each crop has a different success rate and points reward."""
    global points
    global secret
    global rate
    global multiplier
    choice: str = ""
    print(f"------\nWelcome to your farm, {player}!\nBe careful! Unsuccessfully grown crops will lead to a loss in points!")
    while choice != 'x':
        print("------\nWhat crop would you like to grow?")
        if secret is True:
            print(f"s) {SHINE}Shiny Wasabi{SHINE}: 5000 points (success rate: ???)")
        choice = input(f"a) Corn {CORN}: {(int)(5 * multiplier)} points (success rate: {rate + 40}%)\nb) Wheat {WHEAT}: {(int)(8 * multiplier)} points (success rate: {rate + 25}%)\nc) Eggplant {EGGPLANT}: {(int)(18 * multiplier)} points (success rate: {rate}%)\nx) Exit farm\n")
        if choice == 'a':
            if randint(1, 100) <= rate + 40:
                points += (int)(5 * multiplier)
                print(f"You successfully grew corn {CORN}! You now have {points} points!")
            else:
                points -= (int)(2 * multiplier)
                print(f"The attempt to grow corn was unsuccessful. You lost {(int)(2 * multiplier)} points. You have {points} points.")
        elif choice == 'b':
            if randint(1, 100) <= rate + 25:
                points += (int)(8 * multiplier)
                print(f"You successfully grew wheat {WHEAT}! You now have {points} points!")
            else:
                points -= (int)(3 * multiplier)
                print(f"The attempt to grow wheat was unsuccessful. You lost {(int)(3 * multiplier)} points. You have {points} points.")
        elif choice == 'c':
            if randint(1, 100) <= rate:
                points += (int)(18 * multiplier)
                print(f"You successfully grew eggplant {EGGPLANT}! You now have {points} points!")
            else:
                points -= (int)(5 * multiplier)
                print(f"The attempt to grow eggplant was unsuccessful. You lost {(int)(5 * multiplier)} points. You have {points} points.")
        elif choice == 's' and secret is True:
            if randint(1, 100) >= 95:
                points += 5000
                print(f"{SHINE} Of course, you... wait what??? You actually grew a {SHINE}Shiny Wasabi{SHINE}!!! {SHINE}\n{SHINE} You now have {points} points!!! {SHINE}")
            else:
                points -= (int)(50 * multiplier)
                print(f"Of course, you didn't grow a Shiny Wasabi. You should give up now. You lost {(int)(50 * multiplier)} points. You have {points} points.")
        elif choice == 'x':
            print("Exiting farm")
        else:
            print("Invalid choice, try again later.")


def buy(money: int) -> int:
    """Player can buy upgrades for their farm. Will use up points depending on upgrade."""
    global multiplier
    global rate
    global secret
    choice: str = ""
    print(f"------\nWelcome to the shop, {player}.")
    while choice != 'x':
        print(f"------\nYou have {money} points available.\nWhat would you like to buy?")
        choice = input("a) 20 points- Points Multiplier +10% \nb) 50 points- Success Rate +5%\ns) 500 points- Unlock Secret Crop\nx) Exit shop\n")
        if choice == 'a':
            if money >= 20:
                multiplier += 0.1
                money -= 20
                print(f"Successfully increased the multiplier! You now have {money} points left.")
            else:
                print(f"Insufficient points. You currently have {money} points. Try again later.")
        elif choice == 'b':
            if money >= 50:
                rate += 5
                money -= 50
                print(f"Successfully increased the success rate! You now have {money} points left.")
            else:
                print(f"Insufficient points. You currently have {money} points. Try again later.")
        elif choice == 's':
            if money >= 500 and secret is False:
                secret = True
                money -= 500
                print(f"You've unlocked the {SHINE}secret crop{SHINE}! You now have {money} points left")
            elif secret is True:
                print(f"You already have the {SHINE}secret crop{SHINE} silly!")
            else:
                print(f"Insufficient points. You currently have {money} points. Try again later.")
        elif choice == 'x':
            print("Exiting shop")
        else:
            print("Invalid choice, try again later.")
    return money


def main() -> None:
    """Main function, prompts user to choose one of three options. Runs other functions and procedures. Loops until user exits."""
    global points
    greet()
    choice: str = ''
    while choice != 'x':
        choice = input(f"------\nOkay {player}, What do you want to do next?\na) Grow Crops\nb) Purchase Upgrades\nx) Exit Experience\n")
        if choice == 'a':
            """Sends to farm procedure"""
            # Give three options of what to do next
            # 1) Grow crop 
            #   1 - Corn (success rate: 95%, points: 5) 
            #   2 - Wheat (success rate: 80%, points: 8)
            #   3 - Eggplant (success rate: 50%, points: 20)) 
            farm()
        elif choice == 'b':
            """Sends to buy function"""
            # 2) Use Points 
            #   1 - points multiplier + .2
            #   2 - success rate + 5%
            points = buy(points)
        elif choice == 'x':
            """Exits experience"""
            # 3) Exit experience
            print(f"------\nI hope you had fun {player}! See you later!\n-----")
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()