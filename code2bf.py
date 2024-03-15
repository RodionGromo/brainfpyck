import math

# + set [value]
# + out
# + in
# loop
# 	begin
#   end
# + add (value)
# + sub (value)
# + right (value)
# + left (value)
# + text [string]

file = open("code.bpf", "r")
text = file.readlines()
file.close()

_debug = False

parsedBF = ""

def loopValueCalculator(toSetNum: int) -> tuple:
	div = math.sqrt(toSetNum)
	if div - int(div) != 0:
		div = int(div)
	toAdd = toSetNum - (div**2)
	return (int(div), int(toAdd))

def generateLoop(value: int, addAfter: int, sign: str):
	return ">" + ("+" * value) + "[<" + (sign * value) + ">-]<" + ("+" * addAfter) 

def calcAndGenLoop(value, sign):
	v1,v2 = loopValueCalculator(value)
	return generateLoop(v1, v2, sign)

def convertLine(strin: str) -> dict:
	split = strin.split(" ")
	args = []
	if len(split[1:]):
		args = [arg.strip() for arg in split[1:]]
	return {"cmd": split[0].strip(), "args": args}

def parseLine(data: dict) -> None:
	global parsedBF
	command, args = data["cmd"], data["args"]
	if _debug:
		print(command, args)

	if command == "out":
		parsedBF += "."
	elif command == "in":
		parsedBF += ","
	elif command == "add":
		# if 1 or no args, just add, else calc whole loop
		if (len(args) == 0) or (args[0] == "1"):
			parsedBF += "+"
		else:
			val = int(args[0])
			parsedBF += calcAndGenLoop(val, "+")
	elif command == "sub":
		# same as add
		if (len(args) == 0) or (args[0] == "1"):
			parsedBF += "-"
		else:
			val = int(args[0])
			parsedBF += calcAndGenLoop(val, "-")
	elif command == "set":
		if args[0].isnumeric():
			val = int(args[0])
		else:
			if("\\n" in args[0]):
				val = 10
			else:
				val = ord(args[0])
		# set value to 0 then add arg
		parsedBF += "[-]"
		parsedBF += calcAndGenLoop(val, "+")
	elif command == "right":
		if not len(args) or args[0] == "1":
			parsedBF += ">"
		else:
			val = int(args[0])
			parsedBF += ">" * val	
	elif command == "left":
		if not len(args) or args[0] == "1":
			parsedBF += "<"
		else:
			val = int(args[0])
			parsedBF += "<" * val
	elif command == "text":
		for char in " ".join(args[0:]):
			parsedBF += calcAndGenLoop(ord(char), "+")
			parsedBF += ">"
	elif command == "loop":
		if not len(args): raise Exception("Parser error: loop argument not provided")
		if args[0] == "start":
			parsedBF += "["
		elif args[0] == "end":
			parsedBF += "]"

def saveFile():
	output = open("code.bf", "w")
	output.write(parsedBF)
	output.close()

def compileFile(debug=False):
	global _debug
	_debug = debug
	for line in text:
		data = convertLine(line)
		parseLine(data)
		saveFile()
	


