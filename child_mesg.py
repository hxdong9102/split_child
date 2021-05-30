import time
from datetime import datetime


class Msg():

        def __init__(self, name="Demo class", path=r"../test/child_tree/sub_demo"):
            self.name = name
            self.path = path


        def info(self):
            return self.path


        def child_date(self):
            print("Today is: ", datetime.now())
            return time.timezone