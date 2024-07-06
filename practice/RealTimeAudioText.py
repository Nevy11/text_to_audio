from pocketsphinx import AudioFile

# Trying to convert audio to text offline ... so inefficient
def transcribe_audio(audio_file):
    audio = AudioFile(audio_file=audio_file)

    transcribe_text = ""

    for frame in audio:
        transcribe_text += str(phrase) + ' '
    return transcribe_text

def main():
    audio_file = 'conv.wav'

    transcribe_text = transcribe_audio(audio_file)
    print(transcribe_text)