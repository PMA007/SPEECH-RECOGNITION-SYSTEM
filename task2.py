import speech_recognition as sr

def transcribe_audio_from_mic():
    """
    Captures audio from the microphone and transcribes it into text
    using Google's Web Speech API.
    """
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Adjust for ambient noise to improve accuracy
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        # Listen to the audio input from the microphone
        audio = r.listen(source)

    try:
        print("Transcribing...")
        # Use Google Web Speech API to recognize the speech
        # You can specify the language, e.g., language="en-US" for US English
        text = r.recognize_google(audio, language="en-US")
        print(f"You said: \"{text}\"")
        return text
    except sr.UnknownValueError:
        # Handle cases where speech is unintelligible
        print("Sorry, I could not understand audio.")
        return None
    except sr.RequestError as e:
        # Handle API errors (e.g., no internet connection, API key issues)
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    print("Starting Speech-to-Text System...")
    print("---------------------------------")
    transcribed_text = transcribe_audio_from_mic()
    if transcribed_text:
        print("\nTranscription complete.")
    else:
        print("\nTranscription failed or no speech detected.")
