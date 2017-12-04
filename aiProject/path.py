import numpy as np
import random as rnd

class Path():
    def __init__(self,x,y):
        self.path = np.zeros((x,y), dtype=np.int16)
        self.x = x
        self.y = y

    def set_border(self):
        for x in range(self.x):
            self.path[0,x] = 1
            self.path[x,-1] = 1
        for y in range(self.y):
            self.path[y,0] = 1
            self.path[-1,y] = 1

            # set in and out points

    def setInAndOut(self):
        inAndOut = []
        for xy in range(2):
                x = rnd.randint(1,self.x-1)
                y = rnd.randint(1,self.y-1)
                inAndOut.append((x,y))

        if inAndOut[0] == inAndOut[1]:
           self.setInAndOut()
        elif 0 or self.x-1 not in inAndOut[0] or 0 or self.y-1 not in inAndOut[1] :
           self.setInAndOut()
        else:
            self.path[inAndOut[0]] = 2
            self.path[inAndOut[1]] = 2
            print(inAndOut[0])
            print(inAndOut[1])
            return inAndOut[0],inAndOut[1]

    def setThePath(self):
        

    def show_path(self):
        for x in range(self.x):
            for y in range(self.y):
                if self.path[x,y] == 1:
                    print("#",end="")
                elif self.path[x,y] == 2:
                    print("O", end="")
                else:
                    print(" ",end = "")
            print(" ")

bigPath = Path(10,10)
bigPath.set_border()
bigPath.setInAndOut()
bigPath.show_path()

