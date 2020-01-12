from tkinter import * #Tkinter is used to create the GUI of the game

#The amount of groups is tracked, as well as their names and scores. Group names use letters.
groupCount=0
groupLetters=['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U','V','W','X','Y','Z']
groupNames=[]
groupScores=[]

#This determines if the basic setup is active or not.
setUp=False

#This tracks how many levels the game has, and which level the player is currently on.
levels=10
currentLevel=0

#The problems, solutions, and difficulty are matched with each other.
# Regarding difficulty:
# e=easy
# m=medium
# h=hard
problems=[
    ''' find the value of x:
        {2x+6y =20
        {2x+3y =11
       A)x=6  B)x=2  C)x=3  D)x=1 
    ''',
    ''' what is equal to 
        3(x+5)-6
       A)3x-3  B)3x-1  C)3x+9  D)15x-6
       ''',
    ''' what is the solution of
        {x=y-3
        {(x/2)+2y=6
       A)(-3,0)  B)(0,3)  C)(6,-3)  D)(36,-6)
    ''',
    ''' what is equal to 
        (5+12i)-(9i^2-6i)
       A)-14-18i  B)-4-6i  C)4+6i  D)14+18i
    ''',
    ''' what is f(-1)
        f(x)=(x^2-6x+3)/(x-1)
       A)-5  B)-2  C)2  D)5
    ''',
    ''' what is equal to 
        x^2+6x+4
       A)(x+3)^2+5  B)(x+3)^2-5  C)(x-3)^2+5  D)(x-3)^2-5
       ''',
    ''' what is equal to
        (x^2-2x-5)/(x-3)
       A)x-5-((20)/(x-3))  B)x-5-((10)/(x-3))  C)x+1-((8)/(x-3))  D)x+1-((2)/(x-3))  
       ''',
    ''' what is x+4 if
        2x+8=16
       A)8  B)2  C)12  D)4''',
    ''' what is p if
        2(p+1)+8(p-1)=5p
       A)1.8  B)1.2  C)0.8  D)1.6''',
    ''' find the value of y:
        {(1/2)(2x+y)=(21/2)
        {y=2x
       A)5.57  B)5.52  C)5.25  D)5.75'''
]
solutions=['4', '3', '2', '4', '1', '2', '4', '1', '2', '3']
difficulty=['m', 'e', 'm', 'h', 'h', 'h', 'h', 'e', 'e', 'm']

#An increase of points depends on the difficulty
easyPoints=5
mediumPoints=10
hardPoints=15

#This function destroys the initial starting scene.
def groupEnter():
    global groupCount, firstSubmitButton
    try:
        groupCount = int(entryWidget.get())
        firstSubmitButton.pack_forget()
        groupLabel.pack_forget()
        entryWidget.pack_forget()
        group_assign()
    except:
        pass
#This function creates the groups based on the number of groups. Each group has a name and a score allotment.
def group_assign():
    global groupCount, groupScores, groupNames
    for i in range(0, groupCount):
        groupNames.append(groupLetters[i])
    for i in range(0, len(groupNames)):
        groupScores.append(0)
    question_setup()

#This function displays the current problem, where the player can enter an answer in an entry widget.
def question_setup():
    global currentLevel, question, enterInput, firstSubmitButton, setUp
    question.pack_forget()
    if currentLevel==levels:
        finalScreen()
    if currentLevel>levels-1:
        pass
    question=Label(tk, text=problems[currentLevel])
    question.pack()
    enterInput.pack_forget()
    enterInput.pack()
    if setUp == False:
        firstSubmitButton.pack_forget()
        setUp=True

#This is the final screen of the game where previous GUI is deleted. This final screen shows the scores of the players.
def finalScreen():
    global enterInput, groupNames, groupScores
    enterInput.pack_forget()
    for group in range(0, len(groupNames)):
        groupText="Group " + groupNames[group]+": " + str(groupScores[group]) + " pts."
        groupLabel=Label(tk, text=groupText)
        groupLabel.pack()

#This function takes in user input and processes it.
# It also deletes the text in the entry widget for the next question.
# It adds the score depending on difficulty to the correct group.
# Finally, it calls question_setup after increasing currentLevel to show the next question.
#If the input is not valid or is empty, the function will stop.
def processInput(event):
    global currentLevel, enterInput
    try:
        input=enterInput.get()
        if input=='':
            return
        groupLetter=input[0]
        groupIndex=groupNames.index(groupLetter)
        answer=input[1]
        enterInput.delete(0, 'end')
        if currentLevel>levels-1:
            return
        if solutions[currentLevel] != answer:
            currentLevel += 1
            question_setup()
            return
        if difficulty[currentLevel]=='e':
            groupScores[groupIndex] += easyPoints;
        if difficulty[currentLevel]=='m':
            groupScores[groupIndex] += mediumPoints;
        if difficulty[currentLevel]=='h':
            groupScores[groupIndex] += hardPoints;
        currentLevel+=1
        question_setup()
    except:
        pass

#A non-resizable small GUI window is created using Tkinter.
tk=Tk()
tk.geometry("500x150")
tk.resizable(False, False)

#This group label is shown at the beginning to ask how many groups there are.
groupLabel=Label(tk, text="How many groups are there")
groupLabel.pack()

#There is a question label. The text of this label is changed per question.
question=Label(tk)

#This is the beginning entryWidget which asks the user to enter how many groups there are.
entryWidget=Entry(tk)
entryWidget.pack()

#In enterInput, users enter in answers to questions.
enterInput = Entry (tk)

#Everytime the enter key is pressed, the input inside enterInput will be processed.
tk.bind('<Return>', processInput)

#These buttons determine whether the game will use radio buttons or not.
firstSubmitButton=Button(tk, text="Enter", command=groupEnter)
firstSubmitButton.pack()


#This ends the Tkinter application.
tk.mainloop()