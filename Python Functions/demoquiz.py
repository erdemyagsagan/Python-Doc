#Question

class Question:
    def __init__(self,text ,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

q1 = Question('En guzel yemekler hangi ulkenin',['Turkiye','Yunan','ALmanya','Amerika'],'Turkiye')
q2 = Question('En guzel ulke hangi ulke',['Turkiye','Yunan','ALmanya','Amerika'],'Turkiye')
q3 = Question('En unlu yemekler hangi ulkenin',['Turkiye','Yunan','ALmanya','Amerika'],'Turkiye')

print(q1.text,'\n',q1.choices,'\n')
inputAnswer = input(q1.answer)
q1.checkAnswer(inputAnswer)
