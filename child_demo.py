from child_mesg import Msg
import time


msg = Msg()

info = msg.info()
d_t = msg.child_date()


class Demo():
    def dis_play_demo(self):
        print(info)
        print(d_t)



# display = Demo()
# display.dis_play_demo()