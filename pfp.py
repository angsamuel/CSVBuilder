import sys

inputFileName = sys.argv[1]

outputFileName = sys.argv[2]


inputFile = open(inputFileName, "r")
outputFile = open(outputFileName, "w")

for line in inputFile:
	testName = line.split("-")[0]
	filePath = "/home/sam/multithreadingtests/parsec/tests/" + testName + "/"
	fixedLine = filePath + line
	outputFile.write(fixedLine)

inputFile.close()
outputFile.close()