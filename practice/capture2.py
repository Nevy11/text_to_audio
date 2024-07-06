import pyaudio
import wave


"""
Trying to convert the audio of the user from speech to audio file
"""

class Outside2file:
    def __init__(self, rate, channels, input, frames):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            rate= self.rate,
            channels=self.channels,
            format=self.format,
            input=self.input,
            frames_per_buffer = self.frames
        )
