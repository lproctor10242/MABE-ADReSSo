import speech_recognition as sr
from pocketsphinx import AudioFile
import assemblyai as asai


def speechRecognition_sphynx(fileN, segM, offS):
	from os import path
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), fileN)

	# use the audio file as the audio source
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		if offS == 0:
			r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.record(source, segM, offS)
    
    # recognize speech using SphinxassemblyAI
	try:
		return r.recognize_sphinx(audio)
	except sr.UnknownValueError:
		return "Sphinx could not understand aubo"
	except sr.RequestError as e:
		return "Sphinx error; {0}".format(e)

def speechRecognition_google(fileN, segM, offS):
	from os import path
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), fileN)

	# use the audio file as the audio source
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source, segM, offS)
    
    # recognize speech using Google
	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		return "Google could not understand aubo"
	except sr.RequestError as e:
		return "Google error; {0}".format(e)





