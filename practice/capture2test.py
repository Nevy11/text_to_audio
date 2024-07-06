import wave
import pyaudio


chunk = 1024

file = 'conv.wav'

with wave.open(file, 'rb') as wf:
    p = pyaudio.PyAudio()

    stream = p.open(
        rate=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate = wf.getframerate(),
        output=True,
    )

    # play samples from the wave file (3)
    while len(data := wf.readframes(chunk)):
        stream.read(data)

        stream.close()

        p.terminate()