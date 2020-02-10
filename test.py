# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:11:40 2019

@author: nbarl
"""

from algo1 import ksingular, combineTowers, getBlocks, getTowers, towerize, getContacts, step2, step3, algo1
import BinImage
import Evolution
import generation
import time
import matplotlib.pyplot as plt


imageTest = [[0,0,0,0,0,0,0,0,0,0,0,0],
			 
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,1,0,0,0,1,0],
			 [1,1,1,1,1,1,1,1,1,1,1,0],
			 [1,1,0,0,1,1,0,0,1,0,0,0],
			 [0,0,0,1,0,1,0,1,1,0,0,0],
			 [0,0,0,1,1,1,0,1,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0]]
"""

imageTest = [[0,0,0,0,0],
			 [0,1,1,1,0],
			 [0,1,0,1,0],
			 [0,1,1,1,0],
			 [0,0,0,0,0],]


imageTest = [[0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,1,0,0,0,0],
			 [0,1,0,0,0,0,1,1,1,1,1,0],
			 [0,1,1,1,1,1,1,1,1,0,1,0],
			 [0,1,0,1,1,1,0,0,1,0,1,0],
			 [0,0,0,0,0,1,0,0,1,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0]]


imageTest = [[0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [1,0,0,0,0,0,0,0],
			 [1,0,1,0,1,0,0,0],
			 [1,1,1,0,1,1,1,1],
			 [1,0,1,1,1,1,0,1]]



imageTest = [[0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,1,0,0],
			 [0,0,1,0,0,1,0,0],
			 [1,1,1,1,1,1,0,0],
			 [0,0,1,0,1,1,1,0]]
"""

#image = BinImage.BinImage(imageTest, False, True)

"""
image = generation.randomImage(100)
evol = Evolution.Evolution(image)
image.show()

algo1(evol)

print(evol.getNbActions())

#evol.createGif("part1Random.gif", 100)

"""

nbIter = 1
ns = [5,10,20,35, 50, 75]
value = []

for n in ns :
	listOfValues = []
	for i in range(nbIter) :
		print("generating...")
		image = generation.randomImage(n)
		evol = Evolution.Evolution(image)
		print("solving")
		algo1(evol)
		listOfValues.append(evol.getNbActions())
		print(n, " pixels : ", evol.getNbActions(), " actions.")
	value.append(sum(listOfValues) / nbIter)

plt.figure()
plt.plot(ns, value)
plt.show()


