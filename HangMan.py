import random
Word_List = ["tiger","elephant","camel"]
pick_word = random.choice(Word_List)
checkLen = len(pick_word) * 2
pick_word = list(pick_word)
newWord = []

while checkLen > 0 :
    UserInput = input("Enter the letter : ")
    if len(UserInput ) > 1:
       UserInput  = input("Enter only single letter : ")
    
    # if pick_word.find(UserInput):
    #     newWord.
    if UserInput in pick_word :
        loc = pick_word.index(UserInput)
        newWord.insert(loc,UserInput)
        pick_word.remove(UserInput)
    elif UserInput not in pick_word :
        print("Not in list you missed another chance")
    for i in newWord :
        print(i)    
    checkLen -= 1 
    if len(pick_word) == 0:
        checkLen = 0
if len(pick_word) == 0:
    print("You Win")
else :
    print("You loose")