print("\n*** Treasure Island ***\n")

choice1 = input("You find yourself at a crossroads. Which way do you want to go? Type 'left' or 'right':\n").strip().lower()

if choice1 == "left":
    print("\nYou have arrived at a big and deep lake.\n")
    
    choice2 = input("If you want to wait for a boat, type 'wait' or if you want to swim across, type 'swim':\n").strip().lower()
    
    if choice2 == "wait":
        print("\nYou have safely reached an island.\n")
        
        choice3 = input("You find a house with 3 doors: 'red', 'yellow', and 'blue'. Which one do you choose?\n").strip().lower()
        
        if choice3 == "red":
            print("\nYou entered a room full of fire. Game Over!\n")
            
        elif choice3 == "yellow":
            print("\nYou found the treasure! Congratulations, you win!\n")
            
        elif choice3 == "blue":
            print("\nYou entered a room full of crocodiles. Game Over!\n")
            
        else:
            print("\nYou can only choose one of these options: 'red', 'yellow', or 'blue'.\n")
            
    elif choice2 == "swim":
        print("\nYou were bitten by a trout. Game Over!\n")
        
    else:
        print("\nYou can only type 'swim' or 'wait'.\n")
        
elif choice1 == "right":
    print("\nYou fell into a hole. Game Over!\n")
    
else:
    print("\nYou can only choose 'left' or 'right'.\n")