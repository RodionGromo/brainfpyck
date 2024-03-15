# > - move cursor right
# < - move cursor left
# - - decrement cell
# + - increment cell
# . - output data in cell
# , - input data in cell
# [] - loop, check current cell and if it's >0 it iterates
cmdIndex = 0
cellIndex = 0
cells = [0] * 50000
loopIndexes = []

_debug = False

def getLastLoop():
	return loopIndexes[len(loopIndexes)-1]

def printIfDebug(msg, onlyCMDs=True, end="\n"):
	if _debug:
		if not onlyCMDs:
			print("cmd: " + msg, "value: " + str(cells[cellIndex]), "index: " + str(cellIndex), sep=" ", end=end)
			print([cells[i] for i in range(len(cells)) if i < 10])
		else:
			print(msg,end=end)

def runFile(debug=False):
	global _debug, cmdIndex, cells, cellIndex, loopIndexes
	
	_debug = debug

	file = open("code.bf","r")
	text = file.read()
	file.close()

	while cmdIndex < len(text):
		char = text[cmdIndex]
		printIfDebug(char, True, end="")
		if char == "<":
			cellIndex -= 1
			cmdIndex += 1
		elif char == ">":
			cellIndex += 1
			cmdIndex += 1
		elif char == "+":
			cells[cellIndex] += 1
			cmdIndex += 1
		elif char == "-":
			cells[cellIndex] -= 1
			cmdIndex += 1
		elif char == "[":
			if cells[cellIndex] == 0:
				cmdIndex = text.find("]", cmdIndex)+1
			else:
				loopIndexes.append(cmdIndex+1)
				cmdIndex += 1
		elif char == "]":
			if cells[cellIndex] > 0:
				cmdIndex = getLastLoop()
			else:
				del loopIndexes[len(loopIndexes)-1]
				cmdIndex += 1
		elif char == ".":
			printIfDebug(f"\nout: {cells[cellIndex]}",end="\n")
			print(chr(cells[cellIndex]),end="")
			printIfDebug("")
			cmdIndex += 1
		elif char == ",":
			inp = input()
			if inp == "":
				continue
			elif inp.isdigit():
				cells[cellIndex] = int(inp)
			elif(ord(inp) < 256):
				cells[cellIndex] = ord(inp)
			
			cmdIndex += 1

		if cells[cellIndex] > 256:
			cells[cellIndex] = 0
		if cells[cellIndex] < 0:
			cells[cellIndex] = 0
		
	