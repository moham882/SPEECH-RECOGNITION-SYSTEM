import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def transcribe_audio(file_path):
    audio_input, sample_rate = sf.read(file_path)

    if sample_rate != 16000:
        raise ValueError("Please provide audio sampled at 16kHz")

    inputs = processor(audio_input, sampling_rate=16000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return transcription

if name == "main":
    print("Enter path to your audio file:")
    print("Listening to the file...")
    text = transcribe_audio("example.wav")
    print("Transcription:", text)
