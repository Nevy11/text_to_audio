# from pydub import AudioSegment
import speech_recognition as sr


# convert mp3 to wav
#audio = AudioSegment.from_mp3("silence.mp3")
#audio.export("converted_silence.wav", format="wav")

# initialize the speech recongnizer
r = sr.Recognizer()

# Reading audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile("converted.wav") as source:
	audio_text = r.listen(source)


try:
	# Recognize speech using google web speech api
	text = r.recognize_google(audio_text) # look for an offline one
	print('converting audio transcripts into text...')
	print(text)
except Exception as e:
	print(f"Error: {e}")
#finally:
	#print("You are very stupid!!!")