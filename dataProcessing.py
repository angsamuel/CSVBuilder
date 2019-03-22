#array of all the results we're looking for

breakRows = ["NEW ALLOCATIONS", "FREELIST ALLOCATIONS", "DEALLOCATIONS", "LOCK TOTALS", "Thread Contention","Total Memory Usage", "Detailed Lock Usage"]

resultFields = [
"num_sbrk",
"size_sbrk",
"cycles_alloc",
"cycles_allocFFL",
"cycles_free",
breakRows[0],
"allocation cycles",
"allocation faults",
"allocation tlb read misses",
"allocation tlb write misses",
"allocation cache misses",
"num allocation instr",
breakRows[1],
"allocation cycles",
"allocation faults",
"allocation tlb read misses",
"allocation tlb write misses",
"allocation cache misses",
"num allocation instr",
breakRows[2],
"deallocation cycles",
"deallocation faults",
"deallocation tlb read misses",
"deallocation tlb write misses",
"deallocation cache misses",
"num deallocation instr",
breakRows[3],
"num pthread mutex locks",
"num pthread trylocks",
"num pthread spin locks",
"num pthread spin trylocks",
breakRows[4],
"mutex_waits",
"mutex_wait_cycles",
"mutex_trylock_waits",
"mutex_trylock_fails",
"spinlock_waits",
"spinlock_wait_cycles",
"spin_trylock_waits",
"spin_trylock_fails",
"mmap_waits",
"mmap_wait_cycles",
"sbrk_wait_cycles",
"madvise_waits",
"madvise_wait_cycles",
"munmap_waits",
"munmap_wait_cycles",
"mremap_waits",
"mremap_wait_cycles",
"mprotect_waits",
"mprotect_wait_cycle",
"critical_section_counter",
"critical_section_duration",
breakRows[5],
"maxRealMemoryUsage",
"maxRealAllocMemoryUsage",
"maxTotalMemoryUsage",
"realMemoryUsage",
"realAllocatedMemoryUsage",
"totalMemoryUsage",
breakRows[6],
"num sampled accesses",
"total cache bytes accessed",
"total page bytes accessed",
"cache line writes",
"cache owner conflicts",
"avg. cache utilization",
"avg. page utilization"
]

#stores the names of the allocators we're testing
allocatorsList = []

#create a 2d data matrix with a slot for each resultField
dataMatrix = [[] for x in range(0,len(resultFields))] 

#this matrix will keep track of how many results we've averaged so far
countMatrix =[[] for x in range(0,len(resultFields))] 


def processDataFile(dataFile, allocatorName):
	#work with the global fields declared above
	global resultFields
	#global resultRows
	global allocatorsList
	global dataMatrix
	global countMatrix
	
	#let's see if we already have results for this allocator, or if we need a new column
	columnNum = -1
	if allocatorName in allocatorsList:
		columnNum = allocatorsList.index(allocatorName) #set the column num to the index of our allocator in the list
	else: # otherwise w'ere going to make a new column for our allocator
		allocatorsList.append(allocatorName)
		for row in dataMatrix: #set all values to zero by default
			row.append(0)
		for row in countMatrix: #we have seen zero occurences of this before
			row.append(0)
		columnNum = allocatorsList.index(allocatorName)

	currentRow = 0 #the field we should be looking at

	for line in dataFile:
		result = 0 #default value for position in matrix

		if resultFields[currentRow] in line: #if the line of the input file is the correct input
			stringWithData = line.split(resultFields[currentRow])[1]			

			if resultFields[currentRow] not in breakRows: #this is just a label, move on

				#strip our % out of results as a percentage
				stringWithData = stringWithData.replace("%","")
				stringWithData = stringWithData.replace("=","")

				if "avg" in stringWithData: #we're grabbing an average value
					result = float(stringWithData.split("avg")[1])
				elif resultFields[currentRow] == "cache owner conflicts":
					result = float(stringWithData.split("(")[1].replace(")",""))
				else: 
					result = float(stringWithData)

				#place result in correct matrix
				dataMatrix[currentRow][columnNum] = ((dataMatrix[currentRow][columnNum] * countMatrix[currentRow][columnNum]) + result) / (countMatrix[currentRow][columnNum] + 1)
				#indicate that we have averaged in an additional sample
				countMatrix[currentRow][columnNum] += 1


			currentRow += 1

	#print dataMatrix

def createCSV(outputFileName):
	outputFile = open(outputFileName, "w")
	header = ""
	outputFile.write("FIELD LABELS")
	for allocatorName in allocatorsList:
		outputFile.write("," + allocatorName)
	#print header
	outputFile.write("\n")
	for resultFieldIndex in range(0,len(resultFields)):
		rowString = ""
		outputFile.write(resultFields[resultFieldIndex])
		if resultFields[resultFieldIndex] not in breakRows:
		 	for allocatorIndex in range(0,len(allocatorsList)):
		 		outputFile.write("," + str(dataMatrix[resultFieldIndex][allocatorIndex]))
		# 		outputFile.write(dataMatrix[resultFieldIndex][allocatorIndex])
		outputFile.write("\n")
















		#else: #if the input file is out of order, we need to find the correct field


