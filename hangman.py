#Hangman Preston Hudson 12/1/2019 Written in Python

def hangman(word):
    wrong = 0
    stages = ["",
             "_________       ",
             "|               ",
             "|        |      ",
             "|        O      ",
             "|       /|\     ",
             "|       / \     ",
             "                "
             ]
             rletters = list(word)
             board = ["__"] * len(word)
             win = False
             print("Welcome to Hangman")
