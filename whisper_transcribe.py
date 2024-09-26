import os
import whisper

AUDIO_FILE_TO_TRANSCRIBE = "sample-0.mp3"
VIDEO_FILE_TO_TRANSCRIBE = "video-test.mp4"

FILE_TO_TRANSCRIBE = VIDEO_FILE_TO_TRANSCRIBE

# Split the file name and extension
file_name, file_extension = os.path.splitext(FILE_TO_TRANSCRIBE)

# Save the file name in a variable
transcription_file_name = f"{file_name}.txt"

# Load the model (small, medium, large, etc.)
model = whisper.load_model("small")

# Transcribe audio or video file
result = model.transcribe(FILE_TO_TRANSCRIBE)
print(result["text"])
# Write the transcription to a text file
with open(transcription_file_name, "w") as text_file:
    text_file.write(result["text"])