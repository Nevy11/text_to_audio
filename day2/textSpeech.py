import pyttsx3

def text_to_speech(text, output_file):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech (words per minute)
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty('voices')

    # Select a female voice
    for voice in voices:
        if 'georgian' in list(voice.name):
            engine.setProperty('voice', voice.id)
            print('found')
            break

    # Save speech to a file
    engine.save_to_file(text, output_file)

    # Wait for the speech to finish
    engine.runAndWait()

# Text to convert to speech
text = "Hello, you are very stupid!"
print("printing text")
# Output file path
output_file = "converted.wav"

# Convert text to speech and save to file
text_to_speech(text, output_file)
print('done')