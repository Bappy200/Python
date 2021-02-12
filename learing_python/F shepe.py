for row in range(5):
    for col in range(5):
        if(row==0 or row==2):
            print("X",end="")
        elif(col<2):
            print("X",end="")
        else:
            break
    print("")
