
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning..!")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon..!")

	else:
		speak("Good Evening..!")

	assname =("Googly")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you?")
	uname = takeCommand()
	speak("Welcome ")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome ", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you ")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #paste your email id and password in the respective places
    server.login('your email id', 'password') 
    server.sendmail('your email id', to, content)
    server.close()

def getWeather(city_name):
    webbrowser.open("https://www.bing.com/opaluqu/v1?q=weather&input=2&uquresponseformat=1&uqubfprlg=1&form=ANNTH1&refig=07908c59c6f04d79887537b21bee7b26")

def getNews():
    webbrowser.open("https://www.bbc.com/news")
    
    
    def wish():
    print("Wishing.")
    time = int(datetime.datetime.now().hour)
    global uname,asname
    if time>= 0 and time<12:
        speak("Good Morning...!")

    elif time<18:
        speak("Good Afternoon...!")

    else:
        speak("Good Evening...!")

    asname ="Googly"
    speak("I am your Voice Assistant ,")
    speak(asname)
    print("I am your Voice Assistant,",asname)
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takecommand()
    print("Name:",uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)

def takeCommand():
    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing.....")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command

def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")
    
