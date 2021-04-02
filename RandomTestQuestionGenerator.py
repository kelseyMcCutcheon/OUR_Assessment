from random import randint

def replaceVariables(question, variables) ->str:
    for x in variables:
        if x in question:
            question = question.replace(x, str(variables[x]))
    return question

def newVariables(variables, rangeMin=1, rangeMax=9) -> dict:
    for x in variables:
        newInt = randint(rangeMin,rangeMax)
        if newInt == variables[x]:
            while newInt == variables[x]:
                newInt = randint(rangeMin,rangeMax)
        variables[x] = newInt
    #print(variables)
    return variables