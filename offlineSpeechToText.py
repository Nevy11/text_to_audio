from pocketsphinx import AudioFile

def transcribe_audio(audio_file):
    # Initialize PocketSphinx AudioFile with the path to the audio file
    audio = AudioFile(audio_file=audio_file)

    # Transcribe speech
    transcribed_text = ""
    for phrase in audio:
        transcribed_text += str(phrase) + " "

    return transcribed_text.strip()

# Provide the path to your audio file
audio_file = "conv.wav"

# Transcribe the speech in the audio file
transcribed_text = transcribe_audio(audio_file)

# Print the transcribed text
print("Transcribed Text:")
print(transcribed_text)
