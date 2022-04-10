import unittest
import unittest.mock
from tateti import Tateti

class TatetiTest(unittest.TestCase):

#mockeo de input
    #@unittest.mock.patch("builtins.input", return_value='5')
    def test_playermove(self):

        tatetest = Tateti("Testbot")
        position = 5
        tatetest.setmove(position)
        
        self.assertEqual(tatetest.table[1][1], "X")

        del tatetest



    @unittest.mock.patch("builtins.input", return_value='a')
    def test_playermovewrong(self, mock):

        tatetest = Tateti("Testbot")

        position = tatetest.playermove()
        
        self.assertEqual(position, -1)



    def test_table(self):

        iniciate = Tateti("name")

        iniciate.table = [["X", "O", "X"], ["X", "X", "O"], ["O", "O", "X"]]

        iniciate.wincondition()

        self.assertEqual(iniciate.playerwin, 1)


    def testinvertkeys(self):
        iniciate = Tateti("name")

        posix = 3

        posix = iniciate.invertkeys(posix)

        self.assertEqual(posix, 9)

    
    def testmachine(self):
        iniciate = Tateti("name")

        iniciate.table = [["X", "O", " "], ["X", "x", "O"], ["O", "O", "X"]]

        iniciate.machinemove()

        self.assertEqual(iniciate.table[0][2], "O")



if __name__ == '__main__':

    unittest.main()


#mock test