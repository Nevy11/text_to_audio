import speech_recognition as sr

class Audio2Text:
    def __init__(self):
        self.r = sr.Recognizer()
    

    def openFile(self, file):
        with sr.AudioFile(file) as source:
            audio_text = self.r.listen(source)

        try:
            text = self.r.recognize_google(audio_text)
            return text
        except Exception as e:
            print("Error: ", e)
    

def main():
    return Audio2Text().openFile('output.wav')

if __name__ == '__main__':
    print(main())