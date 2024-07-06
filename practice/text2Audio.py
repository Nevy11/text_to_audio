import pyttsx3

class textToSpeech:
    def __init__(self, rate, volume):
        self.rate = rate
        self.volume = volume
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
    
    def test(self):
        print('rate: %s', self.rate)
        print('volume: %s', self.volume)
    

    def saving(self, text, file):
        self.engine.save_to_file(text, file)
        
        # Waiting for the speech to finish processing
        self.engine.runAndWait()



def main():
    conv = textToSpeech(1, 0.9)
    text = "How are you doing?"
    file = 'conv.wav'
    print('starts saving')
    conv.saving(text, file)
    print('endsaving')
    conv.test()


if __name__ == "__main__":
    main()