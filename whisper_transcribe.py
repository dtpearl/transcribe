import os
import whisper
import time
from datetime import timedelta

MEDIA_FOLDER = 'media'
TRANSCRIPTION_SAVE_LOCATION = 'output'
AUDIO_FILE_TO_TRANSCRIBE = "sample-0.mp3"
VIDEO_FILE_TO_TRANSCRIBE = "02-Module 2 - Funnel Rx - Funnel Strategy Blueprints for 6 Common Business Models from Cathy Olson on Vimeo(1).mp4"
VIDEO_FILES_TO_TRANSCRIBE = [
    "03-Module 3 - Funnel Rx - Periodic Table of Funnelbuilding Elements from Cathy Olson on Vimeo.mp4",
    "04-Module 4 - Funnel Rx - Funnel Diagnostics from Cathy Olson on Vimeo.mp4",
    "04-Module 4 - Funnel Rx - Funnel Diagnostics from Cathy Olson on Vimeo(1).mp4"
    ]

# Load the model (small, medium, large, etc.)
model = whisper.load_model("small")

# Print the start time
start_time = time.time()
print(f"Start Time: {time.strftime('%H:%M:%S', time.localtime(start_time))}")

for file in VIDEO_FILES_TO_TRANSCRIBE:
  print(f"Start transcribing: {file}")
  # Print the start time for each file
  loop_start_time = time.time()
  print(f"Start Time: {time.strftime('%H:%M:%S', time.localtime(loop_start_time))}") 
  FILE_TO_TRANSCRIBE = file
  FILE_TO_TRANSCRIBE_WITH_FILE_PATH = f"{MEDIA_FOLDER}/{FILE_TO_TRANSCRIBE}"
  # Split the file name and extension
  file_name, file_extension = os.path.splitext(FILE_TO_TRANSCRIBE)

  # Save the file name in a variable
  transcription_file_name = f"{file_name}.txt"

  # Transcribe audio or video file
  result = model.transcribe(FILE_TO_TRANSCRIBE_WITH_FILE_PATH)

  # Record the loop finish time
  loop_finish_time = time.time()

  # Calculate the duration
  loop_duration = loop_finish_time - loop_start_time

  # Convert duration to minutes and seconds
  duration_formatted = str(timedelta(seconds=loop_duration))

  print(f"Transcription completed for: {FILE_TO_TRANSCRIBE}")

  print(f"Finish Time: {time.strftime('%H:%M:%S', time.localtime(loop_finish_time))}")
  print(f"Duration: {duration_formatted}")

  # Write the transcription to a text file
  with open(f"{TRANSCRIPTION_SAVE_LOCATION}/{transcription_file_name}", "w") as text_file:
      text_file.write(result["text"])

# Record the finish time
finish_time = time.time()

# Calculate the duration
transcription_duration = finish_time - start_time

# Convert duration to minutes and seconds
transcription_duration_formatted = str(timedelta(seconds=transcription_duration))

print(f"Finish Time: {time.strftime('%H:%M:%S', time.localtime(finish_time))}")
print(f"Duration: {transcription_duration_formatted}")