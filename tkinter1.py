
from tkinter import *
from tkinter.font import BOLD
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

## Your question are right or worong
    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view,font=("Arial",20,BOLD), text="Right!")
            right += 1
        else:
            label = Label(view,font=("Arial",20,BOLD), text="Wrong!")
        
        
## If your answer is wrong so exits the game
            window.destroy()
            
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))
## opetion Button

    def getView(self, window):

        view = Frame(window)
        l1= Label(view,font=("Arial",20,BOLD), text=self.question,fg="red").pack()
        
        Button(view,font=("Arial",20,BOLD),text=self.answers[0],width=20, command=lambda *args: self.check("A", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD), text=self.answers[1],width=20,  command=lambda *args: self.check("B", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD),text=self.answers[2],width=20,  command=lambda *args: self.check("C", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Arial",20,BOLD), text=self.answers[3],width=20,  command=lambda *args: self.check("D", view),fg="blue").pack(side=LEFT)
        # Button(font=("Arial",20,BOLD),text="Do you want  50-50 lifeline: ")
        return view
    def unpackView(self, view):
        view.pack_forget()
        askQuestion()
## When your game finish
def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window,font=("Arial",20,BOLD), text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right",fg="red").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

## Question file

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)
 
window =Tk()
label = Label(window,font=("Arial",30,BOLD),text="Welcome to KAUN BANEGA CROREPATI ",fg="red")
label.pack()
window.config(background="black")

## Image  Add

from tkinter import *
from random import randint
img = PhotoImage(file="/home/madhu/Desktop/madhu.png")
image_list = [img]
pick_number = randint(0, 0)
image_label = Label(image = image_list[pick_number])
image_label.pack(pady = 20)

## Start button

button = Button(window,font=("Arial",20,BOLD), text="Start",fg="red", command=askQuestion)
button.pack()
window.mainloop()



