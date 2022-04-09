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
        
        self.assertEqual(position, 0)

        del tatetest


if __name__ == '__main__':

    unittest.main()


#mock test