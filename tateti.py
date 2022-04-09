from random import randint
import os
import time

class Tateti():

    def __init__(self, player):
        self.__player = player
        if player == "":
            self.__player = "The Unknown"
        self.table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = 0
        self.gaming = True
        self.invalidMove = True
        self.playerwin = 0
        self.maxmoves = 0

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
        print ("\nThe game will start in 3 seconds...")
        time.sleep(3)
        
        self.clearscreen()
        
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
        print ("\n{}".format(self.__player), " turn.")
        self.printtable()

        try:
            position = int(input("\n Select a number between 1 and 9 to place your mark: "))
            if position <= 0 or position >= 10:
                raise ValueError ("\nInvalid move, please try again")
            self.turn = 2
            
            if position == 1:
                position = 7
            elif position == 2:
                position = 8
            elif position == 3:
                position = 9
            elif position == 7:
                position = 1
            elif position == 8:
                position = 2
            elif position == 9:
                position = 3
            
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
        self.wincondition()



    def machinemove(self):
        print ("\nRandintBot turn.")
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
        self.wincondition()



    def printtable(self):
        j = 0
        print("\n")
        for i in range(3):
            print ("\t\t\t", self.table[i][j], "|", self.table[i][j+1], "|", self.table[i][j+2])
            if i < 2:
                print ("\t\t\t-----------")
        print("\n")



    def wincondition(self):
        if self.table[0][0] == "X" and self.table[0][1] == "X" and self.table[0][2] == "X":
            self.playerwin = 1
        if self.table[0][0] == "X" and self.table[1][1] == "X" and self.table[2][2] == "X":
            self.playerwin = 1
        if self.table[0][0] == "X" and self.table[1][0] == "X" and self.table[2][0] == "X":
            self.playerwin = 1
        if self.table[0][1] == "X" and self.table[1][1] == "X" and self.table[2][1] == "X":
            self.playerwin = 1
        if self.table[0][2] == "X" and self.table[1][2] == "X" and self.table[2][2] == "X":
            self.playerwin = 1
        if self.table[1][0] == "X" and self.table[1][1] == "X" and self.table[1][2] == "X":
            self.playerwin = 1
        if self.table[2][0] == "X" and self.table[2][1] == "X" and self.table[2][2] == "X":
            self.playerwin = 1
        if self.table[2][0] == "X" and self.table[1][1] == "X" and self.table[0][2] == "X":
            self.playerwin = 1
        
        if self.table[0][0] == "O" and self.table[0][1] == "O" and self.table[0][2] == "O":
            self.playerwin = 2
        if self.table[0][0] == "O" and self.table[1][1] == "O" and self.table[2][2] == "O":
            self.playerwin = 2
        if self.table[0][0] == "O" and self.table[1][0] == "O" and self.table[2][0] == "O":
            self.playerwin = 2
        if self.table[0][1] == "O" and self.table[1][1] == "O" and self.table[2][1] == "O":
            self.playerwin = 2
        if self.table[0][2] == "O" and self.table[1][2] == "O" and self.table[2][2] == "O":
            self.playerwin = 2
        if self.table[1][0] == "O" and self.table[1][1] == "O" and self.table[1][2] == "O":
            self.playerwin = 2
        if self.table[2][0] == "O" and self.table[2][1] == "O" and self.table[2][2] == "O":
            self.playerwin = 2
        if self.table[2][0] == "O" and self.table[1][1] == "O" and self.table[0][2] == "O":
            self.playerwin = 2
        
        if self.playerwin == 1:
            self.printtable()
            print("%s WINS!" % self.__player)
            self.gaming = False
        if self.playerwin == 2:
            self.printtable()
            print("RandintBot WINS!")
            self.gaming = False
        if self.maxmoves == 9:
            self.printtable()
            print ("Tie!")
            self.gaming = False



    def clearscreen(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
