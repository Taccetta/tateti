from random import randint
import os

class Tateti():

    def __init__(self, player):
        self.__player = player
        self.table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = 0
        self.gaming = True
        self.invalidMove = True

    @property
    def player(self):
        return self.__player

    @player.setter
    def regex(self, player):
        self.__player = player

    def __str__(self):
        return '{}'.format(self.__player)

    def game(self):
        print ("\nWelcome to Tic-Tac-Toe!")
        print ("\nPlayer 1 is {}".format(self.__player), "and Player 2 is RandintBot")

        self.turn = self.roll()
        
        self.gaming = True
        while self.gaming == True:
            if self.turn == 1:
                self.playermove()
            else:
                self.machinemove()

    def roll(self):
        turn = randint(1, 2)
        if turn == 1:
            print ("\nPlayer 1 begins.")
        else:
            print ("\nPlayer 2 begins.")
        return turn

    def playermove(self):
        self.printtable()

        try:
            position = int(input("\n Select a number between 1 and 9 to place your mark: "))
            if position <= 0 or position >= 10:
                raise ValueError ("\nInvalid move, please try again")
            self.turn = 2
            
            position -= 1
            mark = 0
            break_out_flag = False
            for i in range(3):
                for j in range(3):
                    if position == mark and self.table[i][j] != " ":
                        raise ValueError ("\nInvalid move, please try again")
                    
                    if position == mark:
                        self.table[i][j] = "X"
                        break_out_flag = True
                        break
                    mark += 1
                if break_out_flag:
                    break

        except ValueError as er:
            self.turn = 1
            print(er)

        self.clearscreen()

    def machinemove(self):
        self.printtable()

        try:
            position = randint(1, 9)
            if position <= 0 or position >= 10:
                raise ValueError 
            self.turn = 1
        
            position -= 1
            mark = 0
            break_out_flag = False
            for i in range(3):
                for j in range(3):
                    if position == mark and self.table[i][j] != " ":
                        raise ValueError ("")
                    
                    if position == mark:
                        self.table[i][j] = "O"
                        break_out_flag = True
                        break
                    mark += 1
                if break_out_flag:
                    break

        except ValueError as er:
            self.turn = 2
            print(er)
        

        self.clearscreen()

    def printtable(self):
        j = 0
        print("\n\n")
        for i in range(3):
            print ("\t\t\t", self.table[i][j], "|", self.table[i][j+1], "|", self.table[i][j+2])
            if i < 2:
                print ("\t\t\t-----------")
        print("\n\n")

    def clearscreen(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")