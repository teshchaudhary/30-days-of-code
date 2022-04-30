import random
sticks = 21

while sticks>0:

    print ("Remaining Sticks: " , sticks)
    comp_turn = random.choice([1,2,3,4])

    if comp_turn>sticks:
            comp_turn= random.choice([1,2,3,4])
            continue

    print("Computer took:",comp_turn)

    if sticks == 1:
            print ("Computer took the last stick, You Win!!")
            break
    print ("You Took: " , (5-comp_turn),"\n")
    sticks -= 5
