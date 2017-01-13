# recognize speech using AT&T Speech to Text
ATT_APP_KEY = "INSERT AT&T SPEECH TO TEXT APP KEY HERE"
ATT_APP_SECRET = "INSERT AT&T SPEECH TO TEXT APP SECRET HERE"
try:
	print("AT&T Speech to Text thinks you said " + r.recognize_att(audio,
	app_key=ATT_APP_KEY, app_secret=ATT_APP_SECRET))
except sr.UnknownValueError:
	print("AT&T Speech to Text could not understand audio")
except sr.RequestError as e:
	print("Could not request results from AT&T Speech to Text service;
{0}".format(e))


#To use the AT&T STT service, you have to obtain an AT&T app key as well as an
#app secret and assign them to the ATT_APP_KEY and the ATT_APP_SECRET constants,
#respectively. You then have to implement the r.recognize_att() function and pass
#audio , app_key , and app_secret as arguments. 
