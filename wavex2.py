import librosa
from vosk import Model, KaldiRecognizer

audio_file = "chatgpt2.wav"
model_path = "vosk-model-small-hi-0.22"

audio, sr = librosa.load("chatgpt2.wav", sr=16000)
model = Model("vosk-model-small-hi-0.22")
rec = KaldiRecognizer(model, sr)

rec.AcceptWaveform(audio)
result = rec.FinalResult()
transcription = result["text"]

print(transcription)