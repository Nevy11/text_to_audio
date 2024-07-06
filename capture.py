import pyaudio
import wave


"""
	 Pyaudio library enables binding between the audio ports in mobile devices 
	 pyaudio can enable the audio to play files and intergrate them into speakers
	 pyaudio (VoIP, formats, 
	 wave 
	 for storing and loading audio files
	 can give sample rate, number of channels, frames, and can also readframes
	 e.g.,
	 with open('audio.wav', 'wb') as f:
	  	audio_file = f.readframes()
	  
	"""


def recorded_audio(filename, duration=5, rate=4000, chunk=1024):	
	p = pyaudio.PyAudio() # Initialize the class
	
	stream = p.open(
		format=pyaudio.paInt16,
		channels=1,
		rate = rate,
		input=True,
		frames_per_buffer=chunk
	) # initailize the stream
	
	print("Recording...")
	
	frames = []
	
	for _ in range(0, int(rate/chunk*duration)):
		data = stream.read(chunk) # collect the audio frames
		frames.append(data) 
	print("Finished recording")
	
	stream.stop_stream() # stop streaming
	stream.close() # close the audio ports
	p.terminate() # close the audio listening
	
	
	wf = wave.open(filename, 'wb') # start writing to the file
	wf.setnchannels(1)	# channels
	wf.setsampwidth(p.get_sample_size(pyaudio.paInt16)) # sample size
	wf.setframerate(rate)	# properties
	wf.writeframes(b''.join(frames))	# write the frames in the list
	wf.close()
	
	
recorded_audio("output.wav", duration=5)
	
	
