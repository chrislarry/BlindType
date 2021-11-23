#!/bin/python
import time, random
chars=["a", "b", "c", "d", "e", "f","g","h", "i", "j", "k" ,"l" ,"m", "n",
       "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
inp=""

avertime=[]
sumaver=0
lifes = 3
points=0
level=1
levelup=0
print("")
print(" -----Blind Type Game-----")
print("")
print(" Get Ready....")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("------GO------- ")
starttime=time.time()
lasttime=starttime
print("")
while inp.lower()!="exit":
    if level==4:
        aver=aver+3-lifes
        print("----------------")
        print("----------------")
        print(" The End.")
        print("----------------")
        print("----------------")
        print(" Average: "+ str(round(aver,2)))
        print("----------------")
        print("----------------")
        if aver < 1.5:
            print(" Exelent")
        elif aver < 3:
            print(" Good")
        elif aver < 5:
            print(" Fare")
        elif aver < 7:
            print(" You can do better")
        else:
            print(" Try again")
        print("----------------")
        print("----------------")
        break

    if levelup==30:
        level+=1
        print("‐-------‐-------")
        print(" Level "+str(level))
        print("‐-------‐-------")
        levelup=0
    getran=""
    getrand=random.choices(chars, k=level)
    for i in getrand:
        getran = getran + i
    inp=input(" Type "+ getran+ " ")
    laptime = round((time.time() - lasttime), 2)
    if inp == getran:
        levelup+=1
        points+=1
        avertime.append(laptime)
        for i in avertime:
            sumaver =i+sumaver
        aver=round(sumaver/len(avertime), 2)
        sumaver=0
        print(" Time: " + str(laptime)+ " Average:"+ str(aver) +" Lifes:"+ str(lifes)+" Points:"+str(points)+" Level:"+str(level))
#        print(avertime)
    else:
        lifes-=1
        if lifes==0:
            print(" Yor score is "+str(points)+"\n Game Over")
            inp ="exit"
        print(" Failed, you have "+ str(lifes) +" lifes.")
    lasttime=time.time()
