import sTranscriptors as speechT
import fileIO



def pocketSphinx(fileCSV, fileWAV):
	segments = fileIO.readCSV(fileCSV)
	for cell in segments:
		if cell[2] == "begin":
			continue
		offset = float(cell[2])/1000
		seg = float(cell[3])/1000 - offset
		segString = speechT.speechRecognition_sphynx(fileWAV, seg, offset)
		cell.append(segString)

	outCSV = fileCSV.split('.')[0] + "_Strans." + fileCSV.split('.')[1]
	fileIO.writeCSV(outCSV, segments)

def googleAPI(fileCSV, fileWAV):
	segments = fileIO.readCSV(fileCSV)
	for cell in segments:
		if cell[2] == "begin":
			continue
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


