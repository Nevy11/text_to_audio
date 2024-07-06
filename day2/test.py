import os
import wave
import pyaudio
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

# Function to record audio
def record_audio(filename, duration=5):
    # Set chunk size of 1024 samples per data frame
    chunk = 1024  
    # Sample format
    FORMAT = pyaudio.paInt16  
    # Number of channels
    channels = 1
    # Sampling rate
    rate = 44100  
    
    p = pyaudio.PyAudio()
    
    # Open a new stream
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    
    print("Recording...")
    
    frames = []
    
    # Record for the given duration
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    
    print("Recording finished.")
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to filter audio (high pass filter example)
def filter_audio(input_file, output_file):
    audio = AudioSegment.from_wav(input_file)
    filtered_audio = audio.high_pass_filter(300)
    filtered_audio.export(output_file, format="wav")

# Function to convert audio to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Recognized Text: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    raw_audio_file = "raw_audio.wav"
    filtered_audio_file = "filtered_audio.wav"

    # Step 1: Record audio
    record_audio(raw_audio_file, duration=5)

    # Step 2: Filter the audio
    filter_audio(raw_audio_file, filtered_audio_file)

    # Step 3: Convert the filtered audio to text
    audio_to_text(filtered_audio_file)

    # Cleanup temporary files
    if os.path.exists(raw_audio_file):
        os.remove(raw_audio_file)
    if os.path.exists(filtered_audio_file):
        os.remove(filtered_audio_file)
