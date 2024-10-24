import whisper

model = whisper.load_model("base")

def get_transcript(audio):
    print(audio)
    return model.transcribe(audio)