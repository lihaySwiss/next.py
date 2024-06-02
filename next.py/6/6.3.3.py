import pyttsx3
#if you also use linux you can use the espeak library
#make sure to install it first by running the command: sudo apt-get install espeak

def read_aloud(text):
    # Create a Text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate of speech (optional)
    engine.setProperty('rate', 160)

    # Set the volume level (optional)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()


def main():
    sentence = "omega bad, sigit is the best"
    read_aloud(sentence)


if __name__ == '__main__':
    main()
