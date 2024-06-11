import random
Word_List = ["tiger","elephant","camel"]
pick_word = random.choice(Word_List)
print(pick_word)
checkLen = len(pick_word) * 2
pick_word = list(pick_word)
temp = pick_word
newWord = []

for i in range(0,len(pick_word)):
    newWord.append("_")
print(newWord)
while checkLen > 0 :
    UserInput = input("Enter the letter : ")
    if len(UserInput ) > 1:
       UserInput  = input("Enter only single letter : ")
    
    # if pick_word.find(UserInput):
    #     newWord.
    
    if UserInput in pick_word :
        loc = pick_word.index(UserInput)
        pick_word[loc]="_"
        if UserInput not in newWord[loc]:
        # newWord.replace(loc,UserInput)
            newWord[loc]=UserInput
    elif UserInput not in pick_word :
        print("Not in list you missed another chance")
    print(newWord)
    checkLen -= 1 
    if "_" not in newWord:
        print("You Won")
        checkLen = 0