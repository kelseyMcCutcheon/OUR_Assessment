EASY_WRONG = 3
EASY_RIGHT = 2
MED_WRONG = 2
MED_RIGHT = 2
HARD_WRONG = 2
HARD_LIMIT = 3

def adaptAlgo(correct, questionNumber, numWrong, numRight):

    section = int(questionNumber/3)
    difficulty = questionNumber % 3

    nextQuestion = 0
    
    if(correct):
        if difficulty == 0:
            if numRight >= EASY_RIGHT:
                difficulty = 1
        elif difficulty == 1:
            if numRight >= MED_RIGHT:
                difficulty = 2
        else:
            if numRight+numWrong >= HARD_LIMIT:
                #print("Moving on to the next section!")
                section += 1
                difficulty = 1
    else:
        if difficulty == 0:
            if numWrong >= EASY_WRONG:
                #print("Moving on to the next section!")
                section += 1
                difficulty = 1
        elif difficulty == 1:
            if numWrong >= MED_WRONG:
                difficulty = 0
        else:
            if  numWrong+numRight >= HARD_LIMIT:
                #print("Moving on to the next section!")
                section += 1
                difficulty = 1
            elif numWrong >= HARD_WRONG:
                difficulty = 2

    nextQuestion = (section * 3) + difficulty
    return nextQuestion


