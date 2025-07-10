# speech_to_text_with_input.py

import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print("Listening to the file...")
            audio_data = recognizer.record(source)

        # ✅ Online API (Google)
        text = recognizer.recognize_google(audio_data)

        # ✅ Uncomment this to use offline method (if installed)
        # text = recognizer.recognize_sphinx(audio_data)

        return text

    except FileNotFoundError:
        return "Error: File not found."
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"API error: {e}"

if __name__ == "__main__":
    # ✅ Ask user for input file path
    file_path = input("Enter path to your audio file: ").strip()

    transcription = transcribe_audio(file_path)
    print("\nTranscription:", transcription)
