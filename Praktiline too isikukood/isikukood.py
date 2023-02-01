import random
from math import *
from OmaMoodul import *

firstdigit=[1,2,3,4,5,6]
ikood=""
while True:
    ikood=input("sisestage sinu isikukood: \n")
    if checklen(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s=sugu(ikood)
        if s=="viga":
            print("------------------------------")
            print("Esimene täht ei ole õige")
        else:
            if sunnipaev(ikood)=="viga":
                print("------------------------------")
                print("2-7 tähed on valesti sisestatud")
            else:
                print("------------------------------")
                print(lause(ikood))

                