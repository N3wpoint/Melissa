#To use IBM STT , use the following code snippet:


# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
try:
	print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio,
	username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
	print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
	print("Could not request results from IBM Speech to Text service;
{0}".format(e))


#When using the IBM STT service, you have to obtain an IBM STT username
#and password, which you assign to the IBM_USERNAME and IBM_PASSWORD constants,
#respectively. You then invoke the r.recognize_ibm() function and pass the audio,
#username, and password as arguments.
