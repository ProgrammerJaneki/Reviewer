import os
import sqlite3
import random
class Subjects:
    # Contains the dictioanry 
    questions = {}

    # We will create a function that will add
    # the terms and definitions on the dictionary
    #def addTD(self,term,definition):
        #self.questions.update({term:definition})
    def __init__(self,term="", definition=""):
        self.term = term
        self.definition = definition

    def printTD(self):
        for i in self.questions:
            print(f"TERM: {i} \nDEFINITION: {self.questions[i]}\n")
    '''
    def runTD(self):
        breaker = False
        cnt = 0
        while not breaker:
            add_term = input("Write the term: ")
            add_def = input("Write the definition: ")
            
            subj1.addTD(add_term,add_def)
            while True:
                con = input("Add another one? (y/n): ")
                if con.upper() == "Y":
                    break
                elif con.upper() == "N":
                    breaker = True
                    os.system("cls")
                    break
                else:
                    print("Wrong input..")
                    continue       
    
    def randomTD(self):
        print("Running randomTD...")
        getDef = []
        out = False
        secOut = False
        getTerm = []
        while not out:
            print("Running while...")
            for i in self.questions:
                getDef.append(self.questions[i]) # Will get all definitions in the questions dictionary
                getTerm.append(i)
            print(getDef[0])
            while not secOut:
                definition = random.sample(getDef,1)
                definition = "".join(definition)
                print(f"\nGuess the term:\n{definition}")
                answer = input("Write your answer: ")
                if answer in getTerm:
                    print(definition)
                    print("Answers in..")
                    print(self.questions[answer])
                    if self.questions[answer] == definition:
                        print("Equal..")
                        print(f"Random Definition: {definition}")
                        print(f"Term: {getTerm} ")
                        print(f"Your answer: {answer} ")
                        out = True
                        secOut = True
                        break
                    elif not self.questions[answer] == definition:
                        print("Not Equal..")
                        print("Wrong Answer!")
                else:
                    print("Cannot be found..")
                    continue
       '''


