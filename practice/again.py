import pyaudio
import wave


def recorded_audio(rate, output_file, chunk, duration):
    p = pyaudio.PyAudio()
    stream = p.open(
        rate=rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=chunk,
    )


    print("Recording...")

    frames = []

    for _ in range(0, int(rate/chunk*duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Stopping...")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # saving the file to the audio file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()



def main():
    recorded_audio(rate=4410, output_file='output.wav', chunk=1024, duration=3)

if __name__ == '__main__':
    main()