import unittest
import time
import clock

class ClockTestCase(unittest.TestCase):
    def setUp(self):
        self.clock = clock.Clock()

    def test_clock_initalise(self):
        """
        Test that all variables of the clock object are initalised to 0.
        """
        self.assertEqual(self.clock.Hour, 0)
        self.assertEqual(self.clock.Minutes, 0)
        self.assertEqual(self.clock.Seconds, 0)

    def test_clock_update(self):
        t = time.localtime()
        self.clock.update()
        self.assertEqual(self.clock.Hour, t[3])
        self.assertEqual(self.clock.Minutes, t[4])
        self.assertEqual(self.clock.Seconds, t[5])

if __name__ == '__main__':
    unittest.main()

#import sys

#sys.path.append('../Analogue_clock')
#import Clock

#from .context import Clock

#from .. import clock

#clock = clock.Clock()

#clock.Update()
#clock.Hour