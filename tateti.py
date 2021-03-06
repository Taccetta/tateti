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
    def naming(self, player):
        self.__player = player

    def __str__(self):
        return '{}'.format(self.__player)



    def game(self):
        print ("\nWelcome to Tic-Tac-Toe!")
        print ("\nPlayer 1 is {}".format(self.__player), "and Player 2 is RandintBot")
        print ("\nStarting...")

        time.sleep(0.5)
        
        self.clearscreen()

        self.turn = self.roll()
        self.printtable()
        self.gaming = True
        while self.gaming == True:
            position = -1
            if self.turn == 1:
                while position < 0 or position >= 10:
                    position = self.playermove()
                    position = self.invertkeys(position)
                    position = self.setmove(position)
                self.clearscreen()
                position = self.wincondition()
                self.printtable()

            else:
                position = self.machinemove()
                self.clearscreen()
                position = self.wincondition()
                self.printtable()




    def roll(self):
        turn = randint(1, 2)
        if turn == 1:
            print ("\nPlayer 1 begins.")
        else:
            print ("\nPlayer 2 begins.")
            time.sleep(1)
        return turn



    def invertkeys(self, posix):
        if posix == 1:
            posix = 7
        elif posix == 2:
            posix = 8
        elif posix == 3:
            posix = 9
        elif posix == 7:
            posix = 1
        elif posix == 8:
            posix = 2
        elif posix == 9:
            posix = 3
        return posix



    def playermove(self):

        print ("\n{}".format(self.__player), " turn.")

        try:
            position = int(input("\nSelect a number between 1 and 9 to place your mark: "))
            if position <= 0 or position >= 10:
                raise ValueError

            self.turn = 2
            
            return position

        except ValueError:
            self.turn = 1
            position = -1
            print ("\nInvalid move, please try again.")
            return position



    def setmove(self, position):

        position -= 1
        mark = 0
        break_out_flag = False

        try:
            for i in range(3):
                for j in range(3):
                    if position == mark and self.table[i][j] != " ":
                        raise ValueError
                    
                    if position == mark:
                        self.table[i][j] = "X"
                        self.maxmoves += 1
                        break_out_flag = True
                        break
                    mark += 1
                if break_out_flag:
                    break
            return position

        except ValueError:
            print ("\nInvalid move, please try again.")
            position = -1
            return position



    def machinemove(self):

        print ("\nRandintBot turn.")

        while self.turn == 2:
            try:
                position = randint(0, 8)
                self.turn = 1

                mark = 0
                break_out_flag = False
                for i in range(3):
                    for j in range(3):
                        if position == mark and self.table[i][j] != " ":
                            raise ValueError ("")
                        
                        if position == mark:
                            self.table[i][j] = "O"
                            self.maxmoves += 1
                            break_out_flag = True
                            break
                        mark += 1
                    if break_out_flag:
                        break
            

            except ValueError as er:
                self.turn = 2



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
            self.maxmoves = 0
            print("%s WINS!" % self.__player)
            self.gaming = False
        if self.playerwin == 2:
            self.maxmoves = 0
            print("RandintBot WINS!")
            self.gaming = False
        if self.maxmoves == 9:
            print ("Tie!")
            self.gaming = False



    def clearscreen(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")



    def __del__(self):
        print('...')


