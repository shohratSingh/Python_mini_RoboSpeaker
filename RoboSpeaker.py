import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo 2.0 Created by Mr.Singh")

    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want me to speak (q to quit): ")
        if x.lower() == "q":
            engine.say('Goodbye, my friend!')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
