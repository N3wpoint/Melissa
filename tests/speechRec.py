#imports module as sr
import speech_recognition as sr

#uses pyaudio commands Microphone and Recognizer
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

#writes sound to a wav file
with open("recording.wav", "wb") as f:
	f.write(audio.get_wav_data())
