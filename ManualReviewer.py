import sqlite3
import random
from time import sleep
import os
from Subjects import Subjects

subjDB = "Subjects"
conn = sqlite3.connect(subjDB + ".db")

# We use whenever we're going to execute
# actions in our database
connCur = conn.cursor()
'''
connCur.execute("""CREATE TABLE CPEN100 (
                term text,
                definition text
                )""")
'''

# Inserting terms and definitions to the database
def insertTD(subj):
    with conn:
        connCur.execute("INSERT INTO CPEN100 VALUES (:term, :definition)", {'term': subj.term, 'definition': subj.definition})

# We will get the definition
def getDef(term):
    connCur.execute("SELECT * FROM CPEN100 WHERE term = :term", {'term': term})
    get_def = connCur.fetchone()
    return get_def[1]

''' Reminder: To get all the values in the table just write  
    connCur.execute("SELECT * FROM CPEN100")
    print(connCur.fetchall())'''
# To get all the terms and definitions
def getAll():
    with conn:
        countNum = 1
        connCur.execute("SELECT term, definition FROM CPEN100")
        allTD = connCur.fetchall()
        print("<=>" * 50)    
        for i in allTD:
            print(f"{countNum}.\tTerm: {i[0]}\n\tDefinition: {i[1]}")
            countNum += 1
        print("<=>" * 50)    

# This is where we will add values in the table when the program is running
# To access this function 
def addTD():
    out = False
    secOut = False
    getAll()
    while not out:
        secOut = False
        addTerm = input("Input term:\n>> ")
        addDef = input("Input definition:\n>> ")
        subj1 = Subjects(addTerm, addDef)
        insertTD(subj1)
        getAll()
        print()
        while not secOut:
            runAgain = input("Add another one? (Y) or (N)\n>> ")
            if runAgain.upper() == "Y":
                secOut = True
                break
            elif runAgain.upper() == "N":
                out = True
                secOut = True
                break
            else:
                print("Wrong input..Please try again")
                secOut = True
                break

# Gives random pair of terms and values
def randomTD():
    with conn:
        correctAns = 0
        wrongAns = 0
        randSample = []
        doneTD = []
        firstOut= False
        #secOut = False
        connCur.execute("Select term, definition FROM CPEN100")
        randTD = connCur.fetchall()
        while not firstOut:
            sleep(0.5)
            os.system('cls')
            secOut = False
            randSample = random.choice(randTD)
            #print(randSample[0])
            if randSample in doneTD:
                continue
            else:
                #randSample = random.choice(randTD)
                doneTD.append(randSample)
                print("-" * (len(randSample[1]) + 30))
                print(f"\tQuestion: {randSample[1]}")
                print("-" * (len(randSample[1]) + 30))
                ansTerm = input(">> ")
                sleep(0.5)
                if ansTerm == randSample[0]:
                    sleep(0.5)
                    print("\nCorrect!")
                    correctAns += 1
                    while not secOut:
                        sleep(0.2)
                        conQ = input("Continue? (Y) or (N)\n>> ")
                        if conQ.upper() == "Y":
                            secOut = True
                            break
                        elif conQ.upper() == "N":
                            sleep(0.5)
                            secOut = True
                            firstOut = True
                            break
                        else:
                            print("Invalid Input..")
                            continue
                else:
                    print("\nIncorrect Answer..")
                    sleep(0.5)
                    doneTD.remove(randSample)
                        
                #print(randSample[1])
         
        '''
        if randTD in doneTD:
            randSample = random.choice(randTD)
            print(randSample)
        else:
            doneTD.append(randTD)
            print(randSample)
        '''

# Remove a specific term in the database
def removeTD(term):
    with conn:
        connCur.execute("DELETE FROM CPEN100 WHERE term = :term", {'term': term})

def removeAll():
        with conn:
                connCur.execute("DELETE FROM CPEN100")

""" The one """
# Add values while the program runs
#addTD()
getAll()
randomTD()
conn.close()

