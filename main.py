from tateti import Tateti
import time

if __name__ == '__main__':

    print ("\n\n(press enter to use default name)")
    iniciate = Tateti(str(input("Insert your name: ")))
    iniciate.game()
    time.sleep(1)
    input("\n\nPress enter to exit...")