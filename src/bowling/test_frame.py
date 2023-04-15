import unittest

from bowling.frame import Frame


class TestFrames(unittest.TestCase):
    def test_score(self):
        frame = Frame(2,5)
        self.assertEqual(7, frame.score())

    def test_is_strike(self):
        frame1 = Frame(10,0)
        self.assertTrue(frame1.is_strike())
        frame2 = Frame(0,10)
        self.assertFalse(frame2.is_strike())

    def test_is_spare(self):
        frame1 = Frame(2,8)
        self.assertTrue(frame1.is_spare())
        frame2 = Frame(0,10)
        self.assertTrue(frame2.is_spare())
        frame3 = Frame(10,0)
        self.assertFalse(frame3.is_spare())
        frame4 = Frame(2,7)
        self.assertFalse(frame4.is_spare())

if __name__ == '__main__':
    unittest.main()
