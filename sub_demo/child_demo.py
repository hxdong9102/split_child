import time
from datetime import datetime


class Demo():

    def __init__(self, name="Demo class", path=r"../test/child_tree/sub_demo"):
        self.name = name
        self.path = path

    def info(self):
        print("My name is: ", self.name)
        print("My path is: ", self.path)

    def date(self):
        print("Today is: ", datetime.now())
        print(time.timezone)