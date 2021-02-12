
while(True):
    comment=input()
    if (comment.upper() == "EXIT"):
        break
    elif (comment.upper() == "HELP"):
        print("start game")
        print("exit game")
        print("stop car")
    elif(comment.upper()=="STOP"):
        print("car is stop")

    elif (comment.upper() == "START"):
        print("car is start")

    else:
        print("missing text")


