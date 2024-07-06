import speech_recognition as sr

r = sr.Recognizer()


audio_file = 'converted.wav'

#audio_file = sr.(audio_file, duration=5)
with open(audio_file, 'rb') as f:
    audio = r.listen(f)

text = r.recognize_google(audio)
print(text)