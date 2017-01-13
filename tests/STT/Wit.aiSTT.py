#If you wish to use Wit.ai STT , use this snippet in place of the try / except clause used in
#the previous code:


# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"
try:
	print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
	print("Wit.ai could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Wit.ai service; {0}".format(e))
	

#While using the Wit.ai service, you have to obtain the Wit.ai key stored in the
#WIT_AI_KEY constant. You use the r.recognize_wit() function to pass the audio and the
#key as arguments. 
