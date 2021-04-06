DIFFICULTY = 1
EASY_WRONG = 3
EASY_RIGHT = 2
MED_WRONG = 2
MED_RIGHT = 2
HARD_WRONG = 2
HARD_LIMIT = 3


class adaptAlgo:
    difficulty = DIFFICULTY
    easyWrong = EASY_WRONG
    easyRight = EASY_RIGHT
    medWrong = MED_WRONG
    medRight = MED_RIGHT
    hardWrong = HARD_WRONG
    hardLimit = HARD_LIMIT

    def reset(self):
        self.difficulty = DIFFICULTY
        self.easyWrong = EASY_WRONG
        self.easyRight = EASY_RIGHT
        self.medWrong = MED_WRONG
        self.medRight = MED_RIGHT
        self.hardWrong = HARD_WRONG
        self.hardLimit = HARD_LIMIT

    def correctAnswer(self):
        if self.difficulty == 0:
            if self.easyRight <= 0:
                self.difficulty = 1
                self.easyRight = 2
            else:
                self.easyRight -= 1
        elif self.difficulty == 1:
            if self.medRight <= 0:
                self.difficulty = 2
                self.medRight = 3
            else:
                self.medRight -= 1
        else:
            if self.hardLimit <= 0:
                print("Moving on to the next section!")
                self.section += 1
                self.reset()
            else:
                self.hardLimit -= 1

    def incorrectAnswer(self):
        if self.difficulty == 0:
            if self.easyWrong <= 0:
                print("Moving on to the next section!")
                self.section += 1
                self.reset()
            else:
                self.easyWrong -= 1
        elif self.difficulty == 1:
            if self.medWrong <= 0:
                self.difficulty = 0
                self.medWrong = 2
            else:
                self.medWrong -= 1
        else:
            if self.hardLimit <= 0:
                print("Moving on to the next section!")
                self.section += 1
                self.reset()
            elif self.hardWrong <= 0:
                self.difficulty = 2
                self.hardWrong = 3
            else:
                self.hardWrong -= 1
                self.hardLimit -= 1

    def getNextQuestion(self, correct: bool) -> int:
        nextQuestion = 0
        if correct:
            self.correctAnswer()
        else:
            self.incorrectAnswer()
        return (self.section * 3) + self.difficulty
