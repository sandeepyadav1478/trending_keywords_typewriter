import sys
import keyboard as ky
import os
import pandas as pd
import time
from pynput.keyboard import Key,Controller
from threading import Thread
from os import path
from packages.break_key import break_key
from packages.list_win import switcher
from packages.winmsg import balloon_tip

#-----------------------------
keywords_import  = "assets/google_trend_keywords.csv"
limit_words = 10
exit_key = "esc"
delay = 0   #in seconds
#----------------------------

br_key = Key.enter
aborted = False
counter = 0

def trigger():
    global aborted
    while not aborted:
        if ky.is_pressed(exit_key):
            aborted = True
            break

def writer():
    global counter,br_key
    if path.isfile(keywords_import) == False:
        print("Can't find file, Please provide a clear way.")
        os._exit(0)
    else:
        
        df = pd.read_csv(keywords_import)
        list_of_key = df.values.tolist()
        if len(list_of_key) < 1:
            print("File don't have any content for writing.")
            quit
            os._exit(0)
        else:
            print("Found data for writing.")
            #break key
            br_key = break_key()
            print("-----------------\n")
            # switching window
            switcher()
            balloon_tip("Select Window","Please select any window for auto typing before it start typing.",5,False)
            print("-----------------\n")
            #Exit key
            print("\n************\nExit key:",exit_key,"\n************")
            # starting count down
            balloon_tip("Final Warning","Please confirm window for typing, otherwise u'll face some trouble.",8,True)
            # starting typing
            kc = Controller()
            for i in list_of_key:
                if aborted or counter > limit_words:
                    break
                kc.type(i[0])
                kc.press(br_key)
                counter += 1
                if delay > 0:
                    time.sleep(delay)
            if aborted:
                print("Process interrupted.")
            elif counter > limit_words:
                print("Limit reached. Update limit for more keywords.")
            print(counter," keywords written.")

if __name__ == "__main__":

    t1 = Thread(target = writer,args=())
    t2 = Thread(target = trigger,args=())

    t1.start()
    t2.start()
