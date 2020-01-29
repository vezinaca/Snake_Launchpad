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


def main():

	mode = None

	# create an instance
	lp = launchpad.Launchpad();

	# check what we have here and override lp if necessary
	if lp.Check( 0, "pro" ):
		lp = launchpad.LaunchpadPro()
		if lp.Open(0,"pro"):
			print("Launchpad Pro")
			mode = "Pro"
			
	elif lp.Check( 0, "mk2" ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0, "mk2" ):
			print("Launchpad Mk2")
			mode = "Mk2"

	elif lp.Check( 0, "control xl" ):
		lp = launchpad.LaunchControlXL()
		if lp.Open( 0, "control xl" ):
			print("Launch Control XL")
			mode = "XL"
			
	elif lp.Check( 0, "launchkey" ):
		lp = launchpad.LaunchKeyMini()
		if lp.Open( 0, "launchkey" ):
			print("LaunchKey (Mini)")
			mode = "LKM"

	elif lp.Check( 0, "dicer" ):
		lp = launchpad.Dicer()
		if lp.Open( 0, "dicer" ):
			print("Dicer")
			mode = "Dcr"
			
	else:
		if lp.Open():
			print("Launchpad Mk1/S/Mini")
			mode = "Mk1"

	if mode is None:
		print("Did not find any Launchpads, meh...")
		return


	# scroll "HELLO" from right to left
	
	'''
	if mode == "Mk1":
		lp.LedCtrlString( "HELLO ", 0, 3, -1 )
	# for all others except the XL and the LaunchKey
	elif mode != "XL" and mode != "LKM" and mode != "Dcr":
		lp.LedCtrlString( "HELLO ", 0, 63, 0, -1 )
	
	'''
	
	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()

	lp.LedAllOn()

	lp.Reset()
	
	#if mode == "Mk1" or mode == "XL":
	#			lp.LedCtrlRaw( random.randint(0,127), random.randint(0,3), random.randint(0,3) )

	#while True:
	#	lp.LedCtrlXY(7,7,1,0)

	#time.wait(10)

	app_done = False

	butHit = 10
	while 1:

		#time.wait( 5 )
		but = lp.ButtonStateRaw()

		lp.LedCtrlRaw(22, 3, 3)
		lp.LedCtrlRaw(0, 3, 0)
		lp.LedCtrlXY(3,3,0,3)

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

		#butHit = 10
		if but != []:
			butHit -= 1
			if butHit < 1:
				break
			print( butHit, " event: ", but )

		#print( butHit, " event: ", but )
		if (but == ([0, True])):
			print("button appuye 0,0")
			break
			#lp.Reset() # turn all LEDs off
			#lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)
			#exit()


	lp.ButtonFlush()
	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)
	print("penis")
	
if __name__ == '__main__':
	main()

