import time

class Clock(object):
    """description of class"""
    Hour = 0
    Minutes = 0
    Seconds = 0

    def update(self):
        """Update the current time variables"""
        t = time.localtime()
        self.Hour = t[3]
        self.Minutes = t[4]
        self.Seconds = t[5]