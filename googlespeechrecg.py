import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

#print("Listening...")

try:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust for ambient noise
        print("Say something...")
        audio = recognizer.listen(source, timeout=60)  # Listen for audio with a timeout of 5 seconds

    query = recognizer.recognize_google(audio, language='en-IN')  # Recognize speech using Google
    print("Recognized:", query)

except sr.WaitTimeoutError:
    print("Timeout: No speech detected within the timeout period.")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as e:
    print("Error: {0}".format(e))