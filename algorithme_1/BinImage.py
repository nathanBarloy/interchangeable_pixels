# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:38:42 2019

@author: nbarl
"""
import matplotlib.pyplot as plt


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


#enumeration representing directions
Direction = enum('Right', 'UpRight', 'Up', 'UpLeft', 'Left', 'DownLeft', 'Down', 'DownRight', 'None')






class BinImage :
    """Class representing a binary image"""
    
    def __init__(self, image, black, white) :
        """constructor of the binary image"""
        self.image = image
        self.n = len(image)
        self.m = len(image[0])
        self.black = black
        self.white = white
        self.nbPixel = 0
        for i in range(self.n) :
            for j in range(self.m) :
                self.nbPixel+=image[i][j]
            
            
    def __iter__(self) :
        for i in range(self.n) :
            for j in range(self.m) :
                yield self.image[i][j]
                
    
    def __str__(self) :
        s = ""
        for i in range(self.n) :
            for j in range(self.m) :
                s += "{} ".format(self.image[i][j])
            s+="\n"
        return s
        
    
    def blackIterator(self) :
        """an iterator for black pixels"""
        for i in range(self.n) :
            for j in range(self.m) :
                if self.image[i][j] : yield [i,j]
                
    
    def whiteIterator(self) :
        """an iterator for white pixels"""
        for i in range(self.n) :
            for j in range(self.m) :
                if not self.image[i][j] : yield [i,j]
    
    
    def printMode(self) :
        """print the mode used for the image"""
        s = "Image of type B" + (self.black*4+4) + "W" + (self.white*4+4)
        print(s)
        
        
    def getPixel(self, i, j) :
        """get the value of the pixel (i,j)"""
        if (i>=0 and i<self.n) :
            if (j>=0 and j<self.m) :
                return self.image[i][j]
            else :
                print("error with j when accessing the image")
        else :
             print("error with i when accessing the image")
                
             
    def getNeighbourCoord(self, i, j, direction) :
        """return the coordinates of the neighbour of (i,j), according
        to the given direction"""
        if direction==0 :
            j+=1
        elif direction==1 :
            i-=1
            j+=1
        elif direction==2 :
            i-=1
        elif direction==3 :
            i-=1
            j-=1
        elif direction==4 :
            j-=1
        elif direction==5 :
            i+=1
            j-=1
        elif direction==6 :
            i+=1
        elif direction==7 :
            i+=1
            j+=1
        return i,j
    
    def getNeighbour(self, p, direction) :
        """return the value  of the neighbour of (i,j), according
        to the given direction"""
        coord = self.getNeighbourCoord(p[0], p[1], direction)
        return self.getPixel(coord[0], coord[1])
    
    def getNeighbours(self, p) :
        """return the list of the neighbours of (i,j)"""
        if self.getPixel(p[0], p[1])==0 : #white case
            mode = self.white
        else :
            mode = self.black
            
        l = []
        for direction in range(0,8,(2-mode)) :
            p2 = self.getNeighbourCoord(p[0], p[1], direction)
            if p2[0]>=0 and p2[0]<self.n and p2[1]>=0 and p2[1]<self.m :
                l.append(p2)
        return l
        
    def get8Neighbours(self, p) :
        l = []
        for direction in range(0,8) :
            p2 = self.getNeighbourCoord(p[0], p[1], direction)
            if p2[0]>=0 and p2[0]<self.n and p2[1]>=0 and p2[1]<self.m :
                l.append(self.getPixel(p2[0], p2[1]))
        return l
        
    def getDirection(p1, p2) :
        """gives the direction to go to p2 from p1"""
        if p1[0]<p2[0] :
            if p1[1]<p2[1] :
                return Direction.DownRight
            elif p1[1]==p2[1] :
                return Direction.Down
            else :
                return Direction.DownLeft
        elif p1[0]==p2[0] :
            if p1[1]<p2[1] :
                return Direction.Right
            elif p1[1]>p2[1] :
                return Direction.Left
            else :
                return None
        else :
            if p1[1]<p2[1] :
                return Direction.UpRight
            elif p1[1]==p2[1] :
                return Direction.Up
            else :
                return Direction.UpLeft
     
    def movePixel(self,  action) :
        """move the pixel (i,j) according to the given direction"""
        i = action[0]
        j = action[1]
        direction = action[2]
        a,b = self.getNeighbourCoord(i,j,direction)
        if self.image[i][j] == self.image[a][b] :
            print("Warning : interchange between 2 pixels with the same color")
        self.image[i][j], self.image[a][b] = self.image[a][b], self.image[i][j]
        #self.show()
    
    
    def show(self) :
        """show a figure of the image"""
        plt.figure()
        e=3
        #creation of the grid
        for i in range(self.n+1) : 
            plt.gca().add_line(plt.Line2D((0,self.m), (i,i), lw=e, color='b'))

        for i in range(self.m+1) : 
            plt.gca().add_line(plt.Line2D((i,i), (0,self.n), lw=e, color='b'))

        for coord in self.blackIterator() :
            x = coord[1]
            y = self.n-coord[0]-1
            plt.gca().add_patch(plt.Rectangle((x,y), 1, 1, fc='k'))
        
        plt.axis('scaled')
        plt.show()
        
    def getContour(self) :
        """return a list that contains all the pixels adjacent to the image"""
        contour = []
        for pix in self.blackIterator() :
            for p2 in self.getNeighbours(pix) :
                if self.getPixel(p2[0], p2[1])==0 :
                    if p2 not in contour :
                        contour.append(p2)
        return contour

    def addPixel(self, p) :
        """add a black pixel"""
        self.image[p[0]][p[1]] = 1
        
    def removePixel(self, p) :
        """removes a black pixel"""
        self.image[p[0]][p[1]] = 0
        
    
    def getWhitePixels(self) :
        """returns the list of all white pixels"""
        l = []
        for i in range(self.n) :
            for j in range(self.m) :
                if self.getPixel(i,j)==0 :
                    l.append((i,j));
        return l
    
    def getBlackPixels(self) :
        """returns the list of all black pixels"""
        l = []
        for i in range(self.n) :
            for j in range(self.m) :
                if self.getPixel(i,j)==1 :
                    l.append((i,j));
        return l
    
    def isConnected(self, whiteMode=False) :
        """check if the image is connect"""
        if whiteMode :
            notVisited = self.getWhitePixels()
            color = 0
        else :
            notVisited = self.getBlackPixels()
            color = 1
        
        waiting = [notVisited.pop()]
        visited = []
        while len(waiting)>0 :
            pix = waiting.pop()
            for neighbour in self.getNeighbours(pix) :
                if self.getPixel(neighbour[0], neighbour[1])==color :
                    if neighbour in notVisited :
                        waiting.append(neighbour)
                        notVisited.remove(neighbour)
            visited.append(pix)
        return (len(notVisited)==0), notVisited


