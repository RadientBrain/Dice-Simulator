import random

def rollIt():
    a=[
    "\t\t|           |\n\t\t|     0     |\n\t\t|           |",
    "\t\t|     0     |\n\t\t|           |\n\t\t|     0     |",
    "\t\t|     0     |\n\t\t|     0     |\n\t\t|     0     |",
    "\t\t|     0     |\n\t\t|  0     0  |\n\t\t|     0     |",
    "\t\t|     0     |\n\t\t|  0  0  0  |\n\t\t|     0     |",
    "\t\t|  0  0  0  |\n\t\t|  0  0  0  |\n\t\t|  0  0  0  |",
    ]
    print("\t\t-------------\n"+random.choice(a)+"\n\t\t------------")


if __name__ == "__main__":
    print("\n\t Hello this is a Dice , follow the instruction to roll it...\n")
    rollIt()
    while(True):
        i = input("\n\tEnter 'y' to roll the dice...or 'q' to quit\t")
        if i == 'y':
            rollIt()
        else :
            print("\n\tThanks for playing...")
            break
