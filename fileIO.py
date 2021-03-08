import csv

def readCSV(fileIn):
	with open(fileIn, newline='') as csvfile:
		#putting all values of the csv file into a list object
		segments = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
		seglist = []
		#making a list of lists containing each row
		for row in segments:
			seglist.append(row)

		return seglist
	    

def writeCSV(fileOut, segments):
	with open(fileOut, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(segments)
