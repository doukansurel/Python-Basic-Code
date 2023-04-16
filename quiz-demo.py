#Question 

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

#Quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score = 0 
        self.questionIndex = 0
    
    
    def checkAnser(self , answer ):
        return self.answer ==answer 



    def getQuestions(self): 
        return self.questions[self.questionIndex]

    def displayQuestions(self):
        print(f"Soru  {self.questionIndex + 1 } : {question.text}")
        
        for q in question.choices:
            print("-"+ q)
        answer = input("Cevap : ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestions()

        if question.checkAnswer(answer):
            self.score += 1 
        self.questionIndex += 1
        
        self.displayQuestions()

    def loadQuestion(self):
        if len(questions) == self.questionIndex:
            self.showScore()    
        else : 
            self.displayQuestions()

    def showScore(self):
        pass

q1 = Question("En kolay programlama dili hangisidir ?" , ["C++","C#","JavaScript","Python"],"Python")
q2 = Question("En popüler programlama dili hangisidir ? " , ["C++","Java","Python","C#"],"Python")
q3 = Question("En çok kazandıran programlama dili hangisidir ? " ,["C++","Java","Python","C#"],"Python")

questions = [q1,q2,q3]

quiz = Quiz(questions)
question = quiz.getQuestions()
quiz.displayQuestions()








