import sys
from dataProcessing import *
import time
import datetime

#open our input with the name of our test files file, 
inputFile = open(sys.argv[1], "r")

#get name of the test we're running from the second command line argument
outputName = sys.argv[2]


#for each test file listed in the input file
for line in inputFile:
	if len(line.rstrip()) > 3: #if we see the name of our test in the file name
		dataFileName = line.replace("\n","")#
		dataFile = open(dataFileName.rstrip(), "r")
		allocatorName = dataFileName.split("-")[1]
		print(allocatorName)
		processDataFile(dataFile,allocatorName) #process the file with that name
		dataFile.close()


#build the name of our output 
timeStamp = time.time()
prettyTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')
createCSV("./results/" + outputName + "-results-" + str(prettyTimeStamp) + ".csv")
