import numpy as np
import scipy.signal as signal
import wave

def filter_audio(input_filename, output_filename, cutoff=1000, fs=44100, order=5):
    # Read the audio file
    with wave.open(input_filename, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()

        # Extract audio data
        audio_data = wf.readframes(n_frames)
        audio_data = np.frombuffer(audio_data, dtype=np.int16)

    # Normalize audio data
    audio_data = audio_data / np.max(np.abs(audio_data))

    # Design a Butterworth filter
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)

    # Apply the filter to the audio data
    filtered_data = signal.lfilter(b, a, audio_data)

    # De-normalize the filtered data
    filtered_data = (filtered_data * np.max(np.abs(audio_data))).astype(np.int16)

    # Write the filtered audio data to a new file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(n_channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(filtered_data.tobytes())

# Filter the recorded audio and save it as filtered_output.wav
filter_audio("output.wav", "filtered_output.wav")
