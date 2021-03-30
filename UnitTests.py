import unittest

class TestTestAdaptationAlgorithm(unittest.TestCase):

    def test_allCorrect(self):

        #I am thinking of this "info" as somthing that could be passed along with each answer given
        info = {
            "SECTION_ID": "7THGRADEMATH",
            "NUM_WRONG": 0,
            "NUM_RIGHT": 0,
            "CURRENT_QUESTION": 1,
            "ANSWER": True
        }

        TAA = new TestAdaptationAlgorithm() #not sure what the best way to implement is yet (might just be a function)
        QIDs = []

        #These are just place holders since The amount of questions untill it shifts to the next might be variable
        exspected = [2,2,2,1,1,1]
        exspected2 = [3,2,2,2,1,1,1]
        notExpected = [2,2,2,2,1,1,1]

        for x in range(6):
            QIDs.insert(0, TAA.getNextQuestion(info))
        
        self.assertEquals(QIDs, exspected)

        QIDs.insert(0,TAA.getNextQuestion(True))
        #testing the jump from one section to another
        self.assertEquals(QIDs, exspected2)
        self.assertNotEquals(QIDs, notExpected)
