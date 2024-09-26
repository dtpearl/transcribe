import os
import whisper
import time
from datetime import timedelta

# Record the start time
start_time = time.time()

# Print the results
print(f"Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")


MEDIA_FOLDER = 'media'
TRANSCRIPTION_SAVE_LOCATION = 'output'
AUDIO_FILE_TO_TRANSCRIBE = "sample-0.mp3"
VIDEO_FILE_TO_TRANSCRIBE = "02-Module 2 - Funnel Rx - Funnel Strategy Blueprints for 6 Common Business Models from Cathy Olson on Vimeo(1).mp4"
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

# Record the finish time
finish_time = time.time()

# Calculate the duration
duration = finish_time - start_time

# Convert duration to minutes and seconds
duration_formatted = str(timedelta(seconds=duration))

print("Transcription completed")

print(f"Finish Time: {time.strftime('%H:%M:%S', time.localtime(finish_time))}")
print(f"Duration: {duration_formatted}")

# Write the transcription to a text file
with open(f"{TRANSCRIPTION_SAVE_LOCATION}/{transcription_file_name}", "w") as text_file:
    text_file.write(result["text"])