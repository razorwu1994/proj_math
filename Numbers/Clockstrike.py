import winsound
import time
import datetime
flag = True

#time control
while flag:
    h = int(time.strftime("%S", time.localtime()))
    if h == 23:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
    else:
        pass

