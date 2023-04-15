import unittest

from bowling.frame import Frame
from bowling.game import BowlingGame


class TestGames(unittest.TestCase):
    def test_new_frame(self):
        frame = Frame(1,5)
        game = BowlingGame()
        game.add_frame(frame)
        self.assertEquals(1, len(game.frames))
        game.add_frame(frame)
        self.assertEquals(2, len(game.frames))
        game.add_frame(frame)
        self.assertEquals(3, len(game.frames))


    def test_score(self):
        game = BowlingGame()
        frame = Frame(1,4)
        game.add_frame(frame)
        self.assertEqual(5, game.score())
        frame = Frame(4,5)
        self.assertEqual(14, game.score())


if __name__ == '__main__':
    unittest.main()
