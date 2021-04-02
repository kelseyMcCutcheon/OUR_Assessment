import unittest
from TestAdaptationAlgorithm import adaptAlgo
from RandomTestQuestionGenerator import replaceVariables, newVariables

class TestTestAdaptationAlgorithm(unittest.TestCase):

    def test_allCorrect(self):

        numWrong = 0
        numRight = 0
        quesitonNum = 1
        correct = True

        QIDs = []

        #These are just place holders since The amount of questions untill it shifts to the next might be variable
        exspected = [2,2,2,1,1,1]
        exspected2 = [4,2,2,2,1,1,1]
        notExpected = [2,2,2,2,1,1,1]

        QIDs.insert(0, adaptAlgo(correct, quesitonNum, numWrong, numRight))

        for x in range(5):
            value = adaptAlgo(correct, QIDs[0], numWrong, numRight)
            if value != QIDs[0]:
                numRight = 0
            else:
                numRight += 1
            QIDs.insert(0, value)
        
        self.assertEquals(QIDs, exspected)

        QIDs.insert(0, adaptAlgo(correct, QIDs[0], numWrong, numRight+1))
        #testing the jump from one section to another
        self.assertEquals(QIDs, exspected2)
        self.assertNotEquals(QIDs, notExpected)

    def test_allFail(self):

        numWrong = 0
        numRight = 0
        quesitonNum = 1
        correct = False

        QIDs = []

        #These are just place holders since The amount of questions untill it shifts to the next might be variable
        exspected = [0,0,0,1,1,1]
        exspected2 = [4,0,0,0,1,1,1]
        notExpected = [0,0,0,0,1,1,1]

        QIDs.insert(0, adaptAlgo(correct, quesitonNum, numWrong, numRight))

        for x in range(5):
            value = adaptAlgo(correct, QIDs[0], numWrong, numRight)
            if value != QIDs[0]:
                numWrong = 0
            else:
                numWrong += 1
            QIDs.insert(0, value)
        
        self.assertEquals(QIDs, exspected)

        QIDs.insert(0, adaptAlgo(correct, QIDs[0], numWrong+1, numRight))
        #testing the jump from one section to another
        self.assertEquals(QIDs, exspected2)
        self.assertNotEquals(QIDs, notExpected)

class TestRandomTestQuestionGenerator(unittest.TestCase):
    def test_getRandomVariables(self):

        variables = {
            "X": 10,
            "Y": 10,
            "Z": 10,
            "W": 10
        }
        lastVariables = {
            "X": -10,
            "Y": -10,
            "Z": -10,
            "W": -10
            }

        for x in range(20):
            variables = newVariables(variables)
            self.assertNotEquals(variables, lastVariables)
            for y in variables:
                self.assert_(variables[y] != lastVariables[y])
                lastVariables[y] = variables[y]
    
    def test_replaceVariables(self):
        
        variables = {
            "X": 9,
            "Y": 8,
            "Z": 7,
            "W": 6
        }

        question = "2X-1Y+Z3W"
        expected = "29-18+736"

        result = replaceVariables(question, variables)

        for x in variables:
            self.assert_(x not in result) 

        self.assertEquals(expected, result)
                   
            


if __name__ == '__main__':
    unittest.main()
