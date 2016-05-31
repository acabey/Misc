#  _   _       _____ _       _      _   
# | | | |_ __ |  ___(_) __ _| | ___| |_ 
# | | | | '_ \| |_  | |/ _` | |/ _ \ __|
# | |_| | | | |  _| | | (_| | |  __/ |_ 
#  \___/|_| |_|_|   |_|\__, |_|\___|\__|
#                      |___/            

 # Figlet captcha breaker
 # Each letter is x * 5 in length. Most lowercase are 6 and uppercase 8

 # Each captcha has 8 characters. Total 48 in length
 # Each character can be split into an array and then compared

def ASCIIToFibMap(inverseMap=None):
	# print "Reached ASCIIToFibMap"
	mapping = {}
	if not inverseMap:
		# Import fonts from standard font file
		alphabet = list('0123456789?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]abcdefghijklmnopqrstuvwxyz{|}')

		#Map each character to its FIGlet
		with open('/home/loading/Documents/Programming/TJCTF/modifiedstandardfont.txt') as stdfonts:
			for letter in alphabet:
				# Fill a 6 row array
				arr = []
				for i in range(0,6):
					line = list(stdfonts.readline())
					while allSpaces(line):
						line = list(stdfonts.readline()) #Skips the line if all are spaces

					line.append(' ') # Makes sure each line ends with a space
					if not i:
						arr.append(tuple(line[1:])) #Removes the first space in the line
					else:
						arr.append(tuple(line[0:]))
				mapping[letter] = tuple(arr)
	else:
		for char in inverseMap.keys():
			mapping[inverseMap[char]] = char
	return mapping

def allSpaces(line):
	for char in line:
		if not char == ' ':
			return False
	return True


def FibToASCIIMap(inverseMap=None):
	# print "Reached FibToASCIIMap"
	mapping = {}
	if not inverseMap:
		return FibToASCIIMap(ASCIIToFibMap())
	else:
		#Reverse the dictionary
		for i in range(len(inverseMap.keys())):
			charVal = inverseMap.keys()[i]
			tupleVal = inverseMap.get(charVal)
			mapping.update({tupleVal:charVal})
		return mapping		

def printFiglet(figletter):
	import sys
	# print "Reached printFiglet"
	#Figletter is a matrix
	for row in figletter:
		sys.stdout.write("".join(row))
	return

def checkXAxis(figInput, yValue):
	# print "Reached checkXAxis"
	for x in range(0, len(figInput[0])): #X is dependent on the amount/ size of the letters
		if figInput[x,yValue] == ' ':
			if checkYAxis(figInput, x):
				return x
	return -1

def checkYAxis(figInput, xValue):
	# print "Reached checkYAxis"
	for y in range(0, len(figInput)): #Y should max out at 5
		if not figInput[xValue, y] == ' ':
			return False
	return True

def parseInput(figInput):
	# print "Reached parseInput"
	# Expecting large matrix of * x 5 size
	# Contains the raw input from the netcat feed
	figLetters = []
	# Go through the x axis of the matrix
	# 	if the value at x is a space, check if the same x value with the next y is a space... continue all the way down
	#		if all values at x, y0-ymax are spaces, remove all values from 0-x, y0-ymax into a sub matrix. Add sub matrix to figLetters
	
	# When an x is found, go through each row and remove the values from 0-x into a new array
	# 	Add each array to a submatrix
	# When all rows are complete, append this submatrix to figLetters
	
	while not len(figInput[0]):
		currX = checkXAxis(figInput,0)
		if not currX == -1:				#If for some reason this fails, rip life
			figLetter=[]
			for i in range(0, len(figInput)):
				figList=[]
				for q in range(0,currX):
					figList.append(figInput[i].pop(q))
				figLetter.append(figList)
			figLetters.append(figLetter)

	# Returns a list containing the submatrices of each figLetter
	return figLetters

def parseFigLetter(figletter, debug=False):
	# print "Reached parseFigLetter"
	# Expecting matrix of 6,8 x 5 size
	# Contains a single figlet letter
	# Returns ASCII character counterpart
	# Kind of uses heuristics?
		# Checks for matches between matrix entries. Returns the most likely match
	mostLikelyIndex = 0
	mostLikelyChar = ''
	mostMatches = 0
	percentMatch = 0

	figcharmap = FibToASCIIMap()
	
	for FIGChar in figcharmap.keys():
		if not len(FIGChar) == len(figletter) and len(FIGChar[0]) == len(figletter[0]):
			continue
		
		else:
			lettermatches = 0
			for x in range(0, len(figletter[0])):
				for y in range(0, len(figletter)):
					if FIGChar[y][x] == figletter[y][x]: lettermatches += 1
			if lettermatches > mostMatches:
				mostMatches = lettermatches
				#mostLikelyIndex = FIGCharIndex
				mostLikelyChar = figcharmap.get(FIGChar)
				percentMatch = float(mostMatches)/float(len(figletter[0])*len(figletter))
	if debug:
		return {'mostLikelyChar': mostLikelyChar, 'mostMatches' : mostMatches, 'percentMatch' : percentMatch}
	else:
		return mostLikelyChar

if __name__ == '__main__':
	myMap = FibToASCIIMap()
	#print myMap
	for Figletter in myMap.keys():
		printFiglet(Figletter)
		print parseFigLetter(Figletter, debug=True)
