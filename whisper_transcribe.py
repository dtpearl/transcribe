import os
import whisper

MEDIA_FOLDER = 'media'
TRANSCRIPTION_SAVE_LOCATION = 'output'
AUDIO_FILE_TO_TRANSCRIBE = "sample-0.mp3"
VIDEO_FILE_TO_TRANSCRIBE = "01-Module 1 - Funnel Rx - The Five Principles Of Funnel Building from Cathy Olson on Vimeo.mp4"
FILE_TO_TRANSCRIBE = VIDEO_FILE_TO_TRANSCRIBE
FILE_TO_TRANSCRIBE_WITH_FILE_PATH = f"{MEDIA_FOLDER}/{FILE_TO_TRANSCRIBE}"
# Split the file name and extension
file_name, file_extension = os.path.splitext(FILE_TO_TRANSCRIBE)

# Save the file name in a variable
transcription_file_name = f"{file_name}.txt"

# Load the model (small, medium, large, etc.)
model = whisper.load_model("small")

# Transcribe audio or video file
result = model.transcribe(FILE_TO_TRANSCRIBE_WITH_FILE_PATH)
print(result["text"])
# Write the transcription to a text file
with open(f"{TRANSCRIPTION_SAVE_LOCATION}/{transcription_file_name}", "w") as text_file:
    text_file.write(result["text"])