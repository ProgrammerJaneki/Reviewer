# We will create a class that will be used for the inserting
# of values in the database on a separate file

class Subjects:
    # will contain the terms and definitions using a dict
    questions = {}

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    # This is where we will add the values in the dict
    def addTD(self, term, definition):
        self.questions.update({term:definition})

    def printTD(self):
        for i in self.questions:
            print(f"TERM: {i}\nDEFINITION: {self.questions[i]}")
