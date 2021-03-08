#defines functions for using different transcription methods
import sTranscriptors as speechT
#defines funtions for reading and writing csv files
import fileIO


#function for interpreting via pocketsphinx
def pocketSphinx(fileCSV, fileWAV):
	segments = fileIO.readCSV(fileCSV)
	#getting a list of each row
	for cell in segments:
		if cell[2] == "begin":
			continue
		#setting offset and segment length
		offset = float(cell[2])/1000
		seg = float(cell[3])/1000 - offset
		segString = speechT.speechRecognition_sphynx(fileWAV, seg, offset)
		cell.append(segString)

	outCSV = fileCSV.split('.')[0] + "_Strans." + fileCSV.split('.')[1]
	fileIO.writeCSV(outCSV, segments)

#function for interpreting via googleAPI
def googleAPI(fileCSV, fileWAV):
	#getting a list of each row
	segments = fileIO.readCSV(fileCSV)
	for cell in segments:
		if cell[2] == "begin":
			continue
		#setting offset and segment length
		offset = float(cell[2])/1000
		seg = float(cell[3])/1000 - offset
		segString = speechT.speechRecognition_google(fileWAV, seg, offset)
		cell.append(segString)

	outCSV = fileCSV.split('.')[0] + "_Gtrans." + fileCSV.split('.')[1]
	fileIO.writeCSV(outCSV, segments)


pocketSphinx("adrso024.csv", "adrsonew1.wav")
print("sphinx done")

googleAPI("adrso024.csv", "adrsonew1.wav")
print("google done")


