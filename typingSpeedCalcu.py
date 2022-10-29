from time import *
import random as r
from turtle import speed

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        except :
            error = error+1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay,2)
    speed = len(userinput) /time_R
    return round(speed)



test = ["An iterator is any object in Python which has a next (Python2) or __next__ method defined. That s it.", "That s an iterator.","Now let s understand iteration."]

test1 = r.choice(test)
print("Typing Speed Calculater")
print(test1)
time_1 = time()
testinput = input("Enter : ")
time_2 = time()

print("Speed : " ,speed_time(time_1,time_2,testinput), " w/sec")
print("Error : ", mistake(test1,testinput))