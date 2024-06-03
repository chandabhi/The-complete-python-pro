print("Welcome to treasure island.")
print("your mission is to find tresure")
dir = input('you\'re at a crossroad , where do yuo want to go?"left" or "right".')
if dir == "right":
    print("Game Over")
else :
    next = input('you want to "swim" or "wait"')
    if next == "swim":
       print("Game Over")
    else :
        door = input('Which door to open? "Red","Yellow" or "Blue"')
        if door == "Red":
            print("Game Over")
        elif door == "Yellow":
            print("You Win!")
        elif door == "Blue":
            print("Game Over")
        else : 
            print("Game Over")
