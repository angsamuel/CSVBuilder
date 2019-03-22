import sys
from dataProcessing import *
import time
import datetime

#open our input file, 

inputFile = open(sys.argv[1], "r")
testName = sys.argv[2]

for line in inputFile:
	if testName in line:
		dataFileName = line.replace("\n","")
		dataFile = open(dataFileName, "r")
		allocatorName = dataFileName.split("-")[1]
		processDataFile(dataFile,allocatorName)
		dataFile.close()

timeStamp = time.time()
prettyTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

createCSV("./results/" + testName + "-results-" + str(prettyTimeStamp) + ".csv")
