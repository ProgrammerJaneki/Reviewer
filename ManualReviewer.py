import sqlite3
import random
from time import sleep
import os
from Subjects import Subjects

# We will create the database first
subjDB = "Subjects"
conn = sqlite3.connect(subjDB + ".db")

# The cursor will be used whenever we want to
# execute action in our database
connCur = conn.cursor()

#######################################################################
# ALL FUNCTIONS
#
# We will try to create a function that can create a Table
# while the program is running
def createTable():
    out = False
    while not out:
        print()
        tableName = input("Create a table:\n>> ").replace(" ","")
        if checkTable(tableName) == True:
            connCur.execute(f"""CREATE TABLE IF NOT EXISTS {tableName} (
                            term text, definition text )""")
            out = True
            break

        else:
            print("Table already exists. Please try again.")

# Insert term and definition
def insertTD(subj, table):
    with conn:
        connCur.execute(f"INSERT INTO {table} VALUES (:term, :definition)", {'term':subj.term, 'definition': subj.definition})

# Prints the term and definition of the table
def getTD(table):
    sleep(0.5)
    with conn:
        countNum = 1
        connCur.execute(f"SELECT term, definition from {table}")
        allTD = connCur.fetchall()
        if len(allTD) == 0:
            print("\nTable is empty")
        else:
            print()
            print("<=>" * 50)
            for i in allTD:
                print(f"{countNum}.\tTerm: {i[0]}\n\tDefinition: {i[1]}")
                countNum += 1
            print("<=>" * 50)

# The function will let user add values while the program is running
def addTD(table):
    out = False
    setOut = False
    getTD(table)
    while not out:
        secOut = False
        addTerm = input("\nInput term:\n>> ")
        addDef = input("Input definition:\n>> ")
        subj1 = Subjects(addTerm, addDef)
        insertTD(subj1,table)
        getTD(table)
        print()
        while not secOut:
            runAgain = input("Add another one? (Y/N)\n>> ")
            if runAgain.upper() == "Y":
                secOut = True
                break
            elif runAgain.upper() == "N":
                secOut = True
                out = True
                break
            else:
                print("Wrong input..Please try again")
                continue
            

# To check if table exists
def checkTable(table):
    listTables = connCur.execute(f"SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{table}';").fetchall()
    if listTables == []:
        # Table can be created
        return True
    else:
        return False
        
def getOut():
    sleep(0.5)
    out = False
    while not out:
        choice = int(input("\n\t\t1.) Exit the program\t\t2.) Menu\n>> "))
        if choice == 1:
            out = True
            sleep(0.5)
            return True
        elif choice == 2:
            out = True
            sleep(0.5)
            return False
        else:
            print("Please only input 1 or 2")

# List all the tables in the database
def getAllTables():
    sleep(0.5)
    os.system('clear')
    cnt = 1
    listTables = connCur.execute("SELECT name FROM sqlite_master WHERE type = 'table';").fetchall()
    if listTables == []:
        print("No Table available")
    else:
        for i in listTables:
            print(f"Table {cnt}: {i[0]}")
            cnt += 1

# The reviewer
def randomTD(table):
    sleep(0.5)
    os.system('clear')
    with conn:
        correctAns = 0
        wrongAns = 0
        countWrong = 0
        randSample = []
        doneTD = []
        firstOut= False
        #secOut = False
        connCur.execute(f"SELECT term, definition FROM {table}")
        randTD = connCur.fetchall()
        while not firstOut:
            sleep(0.5)
            os.system('clear')
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
                    countWrong = 0
                    print("\nCorrect!")
                    correctAns += 1
                    while not secOut:
                        sleep(0.2)
                        conQ = input("\nContinue? (Y) or (N)\n>> ")
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
                    wrongAns += 1
                    countWrong += 1
                    sleep(0.5)
                    doneTD.remove(randSample)
                    print()
                    if countWrong >= 3:
                        while not secOut:
                            sleep(0.2)
                            conQ = input("\nThree consecutive wrong answers. Continue? (Y) or (N)\n>> ")
                            if conQ.upper() == "Y":
                                secOut = True
                                countWrong = 0
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
                        pass
        print()
        sleep(0.2)
        print(f"Correct Answers: {correctAns}")
        print(f"Wrong Answers: {wrongAns}")

def removeTable(table):
    connCur.execute(f"DROP TABLE IF EXISTS {table} ")
    getAllTables()

# Remove term and definition
def removeTD(term,table):
    with conn:
        connCur.execute(f"DELETE FROM {table} WHERE term = :term", {'term': term})
    getTD(table)

# Remove all values
def removeAllTD(table):
    with conn:
        connCur.execute(f"DELETE FROM {table}")

#
#######################################################################

# Where we will use the functions
subj1 = Subjects("","")
mainOut = False
while not mainOut:
    sleep(0.5)
    os.system('clear')
    print("#" * 110)
    print("\n\t1.) Create Table\t2.) Choose Table\t3.) List all Tables\t4.) Insert Values\n\t5.) List all values\t6.) Reviewer\t\t7.) Remove Table\t8.) Remove values\n\t\t\t9.) Remove all values\t\t\t10.) Exit\n")
    print("#" * 110)
    runReviewer = int(input(">> "))
    if runReviewer == 1:
        getAllTables()
        createTable()
        mainOut = getOut()
    elif runReviewer == 2:
        getAllTables()
        mainOut = getOut()
        sleep(0.5)
        os.system('clear')
    elif runReviewer == 3:
        getAllTables()
        mainOut = getOut()
    elif runReviewer == 4:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        addTD(selectTable)
        mainOut = getOut()
    elif runReviewer == 5:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        getTD(selectTable)
        mainOut = getOut()
    elif runReviewer == 6:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        randomTD(selectTable)
        mainOut = getOut()
    elif runReviewer == 7:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        removeTable(selectTable)
        mainOut = getOut()
    elif runReviewer == 8:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        getTD(selectTable)
        selectTerm = input("\nDelete term:\n>> ")
        removeTD(selectTerm,selectTable)
        mainOut = getOut()
    elif runReviewer == 9:
        getAllTables()
        selectTable = input("\nSelect Table:\n>> ").replace(" ","")
        removeAllTD(selectTable)
        mainOut = getOut()
    elif runReviewer == 10:
        sleep(0.5)
        mainOut = True
        break


conn.close()

