from tateti import Tateti
import time

if __name__ == '__main__':

    print ("\n\n(press enter to use default name)")
    iniciate = Tateti(str(input("Insert your name: ")))
    name = iniciate.player
    
    iniciate.clearscreen()
    iniciate.game()
    again = input("\nPlay again? (Y/N): ")
    while again == "Y" or again == "y":
        del iniciate
        iniciate = Tateti(name)
        iniciate.clearscreen()
        iniciate.game()
        again = input("\nPlay again? (Y/N): ")
    
    time.sleep(1)
    input("\n\nPress enter to exit...")