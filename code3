if __name__ == '__main__':

    uname=''
    asname=''
    os.system('cls')
    wishMe()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "googly" in command:
            wish()
            
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)
        
        elif 'fine' in command or "good" in command or 'i am fine' in command or 'i am good' in command:
            speak("nice :)")
            
        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" +command)
            speak("Thank you for wishing me! Hope you are doing well!")

       
        elif "who are you" in command:
            speak("I am your desktop voice assistant and my name is Googly.")
        
        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif "what's your name" in command:
            speak("People call me")
            speak(assname)
        
        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)

        elif 'wikipedia' in command:
            speak('Searching Wikipedia')
            webbrowser.open("https://www.wikipedia.org/")
            time.sleep(5)

        elif 'open youtube' in command:
            speak("The Youtube is opening\n")
            print("The Youtube is opening\n")
            webbrowser.open("youtube.com")
            time.sleep(5)

        elif 'open google' in command:
            speak("Google is Opening now\n")
            print("Google is Opening now..!!\n")
            webbrowser.open("google.com")
            time.sleep(5)

        elif 'tell one joke' in command or 'tell me a joke' in command:
            speak("sure, i will!")
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
            
        elif 'mail' in command:
            try:
                speak("To Whom should I send the mail")
                to = input()
                speak("What is the body?")
                content = input()
                sendEmail(to, content)
                speak("Email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("I am sorry, not able to send this email")

    
        elif "do you know me" in command:
            speak("Yes i know about you!")
            
        elif "weather" in command:
            speak(" Please tell me your city name ")
            cityName = takeCommand()
            print("City name : " ,cityName)
            getWeather(cityName)
            time.sleep(5)


        elif 'news' in command or "today's news" in command:
            speak("Today's news ")
            getNews()
            print("Today's news ")
            time.sleep(5)

        elif "camera" in command or "take a photo" in command:
            speak("Smile please")
            print("Smile please :)")
            ec.capture(0, "Googly's Camera ", "img.jpg")
        
        elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                shutdown()
                
        elif 'restart the system' in command or "restart" in command:
                speak("Hold On a Sec ! Your system is on its way to restart")
                restart()

        elif "write a note" in command:
            file = open('C:\\Users\\sahana\\OneDrive\\Desktop\\new.txt', 'w')
            speak("What should i write ")
            note = takeCommand()
        
        elif "open a file" in command:
            speak("Give a file path to be open")
            file_name = input()
            file = open(file_name)
            
                
        elif "are you married or unmarried" in command:
            speak("no im not human to marry someone!!")
            
        elif "I miss you" in command:
            speak("i miss you too!!")
            
        elif 'play music' in command or "play a song" in command:
            speak("Enjoy the music!")
            print("Enjoy the music!")
            music_dir = "C:\\Users\\sahana\\music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1])) 
        
        elif 'images' in command or 'pictures' in command:
            speak("opening images!")
            img_dir="C:\\Users\\sahana\\OneDrive\\Pictures\\Saved Pictures"
            images=os.listdir(img_dir)
            random=os.startfile(os.path.join(img_dir,images[1]))
            
        elif "bye" in command or "good bye" in command:
                speak("Good bye,Have a nice day")
                break
        else:
            speak("Sorry, I am not able to understand you")
            
        
