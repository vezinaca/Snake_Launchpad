#!/usr/bin/env python
#
# Quick usage of "launchpad.py", LEDs and buttons.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
# 
#
# FMMT666(ASkr) 7/2013..2/2018
# www.askrprojects.net
#

import sys
import time

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")

import random
from pygame import time

import pygame

clock = pygame.time.Clock()

wall_x_droite = [7,23,39,55,71,87,103,119]
wall_x_gauche = [0,16,32,48,64,80,96,112]
wall_y_up = [0,1,2,3,4,5,6,7]
wall_y_down = [112,113,114,115,116,117,118]

class Cell(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super(Cell, self).__init__()
		self.x = x
		self.y = y

	def __str__(self):
		return "\tcell (%d,%d)\n"% (self.rect.x, self.rect.y)

class Food(pygame.sprite.Sprite):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def setNewPos(self, snake_coord):
		coordFoodValid = False
		while not coordFoodValid:
			self.rect.x = random.randrange(SIZE[0] - self.largeur)
			self.rect.y = random.randrange(SIZE[1] - self.largeur)
			coordTmp = self.rect.x, self.rect.y
			if coordTmp not in snake_coord:
				coordFoodValid = True

class Score(object):
	def __init__(self, pointage = 0, x = 8, y = 0):
		self.pointage = pointage
		self.x = x
		self.y = y


class Snake(object):

	def __init__(self, x = 3, y = 3, direction = "right"):
		self.coord = []
		self.sprite_snake_list = pygame.sprite.Group()
		self.x = x
		self.y = y
		self.head = Cell(self.x, self.y)
		self.coord.append(self.head)
		self.direction = direction
		self.previousTail = None
		self.step = 1

	def explose(self, message):
		boom = FONT_40.render(message, True, WHITE)
		#screen.blit(theScoreP1, 50, 5)
		screen.blit(boom, (SIZE[0]/2, SIZE[1]/2))
		self.killSnake()

	def killSnake(self):
		for cell in self.coord:
			cell.kill()
		
	def grow(self, allSpritesList):
		newCell = Cell(self.previousTail[0], self.previousTail[1])
		self.coord.append(newCell)
		self.sprite_snake_list.add(newCell)
		allSpritesList.add(newCell)
		

	def createTail(self, longueur):
		tmp = self.startX
		for i in range (0,longueur):
			cell = Cell(tmp- DIMENSION_CELL - self.spaceBetweenCells, self.startY)
			tmp = tmp - DIMENSION_CELL - self.spaceBetweenCells
			self.coord.append(cell)
			self.sprite_snake_list.add(cell)
			#all_sprites_list.add(cell)
		#print self

#wall_y_up = [0,1,2,3,4,5,6,7]
#wall_y_down = [112,113,114,115,116,117,118]


	def isAtWall(self):
		if self.x > 8 and self.direction == "right":
			self.x = 8
			self.direction = "left"
			return True
		elif self.x < 0 and self.direction == "left":
			self.x = 0
			self.direction = "right" 
			return True
		elif self.y < 0 and self.direction == "up":
			self.y = 0
			self.direction = "down"
			return True
		elif self.y > 8 and self.direction == "down":
			self.y = 8
			self.direction = "up"
			return True
		else:
			return False
		
	def update(self):
		if not self.isAtWall():
			if self.direction == "left":
	 			self.x = self.x - self.step
	 		if self.direction == "right":
	 			self.x = self.x + self.step
	 		if self.direction == "down":
	 			self.y = self.y + self.step
	 		if self.direction == "up":
	 			self.y = self.y - self.step
			
 	def __str__(self):
 		tmp = ""
 		for i in range(0,len(self.coord)-1):
 			print self.coord[i]
 		return tmp

def main():

	x = 0
	y = 0

	pygame.init()
	mode = None

	snake = Snake(x, y, "right")
	food = Food(7,7)
	score = Score()

	# create an instance
	lp = launchpad.Launchpad();

	lp.Open()
	print("Launchpad Mk1/S/Mini")
	mode = "Mk1"
	
	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()

	lp.LedAllOn()

	lp.Reset()
	
	app_done = False

	butHit = 120

	while not app_done:

		#but = lp.ButtonStateRaw()
		but = lp.ButtonStateXY()
		lp.LedCtrlXY(snake.x, snake.y, 0, 3)
		lp.LedCtrlXY(food.x, food.y, 3, 0)
		'''
		LED functions

		LedGetColor( red, green )
		LedCtrlRaw( number, red, green )
		LedCtrlXY( x, y, red, green )
		LedCtrlRawRapid( allLeds )
		LedCtrlRawRapidHome()
		LedCtrlAutomap( number, red, green )
		LedAllOn()
		LedCtrlChar( char, red, green, offsx = 0, offsy = 0 )
		LedCtrlString( str, red, green, dir = 0 )

		Button functions

		ButtonChanged()
		ButtonStateRaw()
		ButtonStateXY()
		ButtonFlush()
		'''		
		'''
		if (lp.ButtonStateXY() == ([0 ,1 ,True])):
			print("button appuye 0,0")
			app_done = True
			break
		'''


		#butHit = 10
		if but != []:
			butHit -= 1
			if butHit < 1:
				app_done = True
				break
			print( butHit, " event: ", but )




		#print( butHit, " event: ", but )
		#if (but == ([0, True])):
		if (but == ([0, 1, True])):
			print("button appuye 0,0")
			break
			#lp.Reset() # turn all LEDs off
			#lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)
			#exit()

		#up 200 112
		if (but == ([0, 8, True])):
			snake.direction = "up"
			print("button appuye 200")
			#snake.y = snake.y -1

		#down 201 113
		elif (but == ([1, 8, True])):
			snake.direction = "down"
			print("button appuye 201")
			#snake.y = snake.y + 1

		#left 202 114
		elif (but == ([2, 8, True])):
			snake.direction = "left"
			print("button appuye 202")
			#snake.x = snake.x -1
		#right 203 115
		elif (but == ([3, 8, True])):
			snake.direction = "right"
			print("button appuye 203")
			#snake.x = snake.x + 1

		if(snake.x == food.x and snake.y == food.y):
			score.pointage = score.pointage + 1
			lp.LedCtrlXY(score.x, score.pointage, 0, 3)
		
		snake.update()

		print(snake.x, snake.y, snake.direction)

		clock.tick(4)
		#time.wait(1)
		#lp.ButtonFlush()
		lp.Reset() # turn all LEDs off

	lp.ButtonFlush()
	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)
	print("penis")

	
if __name__ == '__main__':
	main()

