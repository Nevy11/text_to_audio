import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f'Voice: {index}')
    print(f' ID: {voice.id}')
    print(f' Name: {voice.name}')
    #print(f' Description: {voice.description}')
    print(f' Gender: {voice.gender}')
    print(f' Languages: {voice.languages}')
engine.stop()