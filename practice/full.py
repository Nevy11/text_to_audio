import os
import pyaudio
import wave
import speech_recognition as sr

class GetAudio:
    def __init__(self, channels, rate, chunk, duration, outputFile):
        self.rate = rate
        self.chunk = chunk
        self.channels = channels
        self.duration = duration
        self.outputFile = outputFile
        self.p = pyaudio.PyAudio()
        self.frames = []

        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
            input_device_index=None,  # Adjust this if you have multiple input devices
        )

    def recording(self):
        print('Recording...')
        
        try:
            for _ in range(0, int(self.rate / self.chunk * self.duration)):
                data = self.stream.read(self.chunk, exception_on_overflow=False)
                self.frames.append(data)
        except Exception as e:
            print(f"Recording error: {e}")
        
        print('Finished recording')
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
    
    def saving(self):
        wf = wave.open(self.outputFile, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

class GetText:
    def __init__(self, file):
        self.r = sr.Recognizer()
        self.file = file
    
    def audio2Text(self):
        with sr.AudioFile(self.file) as source:
            audioText = self.r.listen(source)
        
        try:
            text = self.r.recognize_google(audioText)
            return text
        except Exception as e:
            return f"Error: {e}"

def main():
    channels = 1
    rate = 4410
    chunk = 1048  # Increased buffer size to reduce overflow risk
    duration = 5
    outputFile = 'audio.wav'

    get_audio = GetAudio(
        channels,
        rate,
        chunk,
        duration,
        outputFile
    )

    get_audio.recording()
    get_audio.saving()

    get_text = GetText(outputFile)
    transcribed_text = get_text.audio2Text()
    print("Transcribed Text:")
    print(transcribed_text)

if __name__ == "__main__":
    main()
