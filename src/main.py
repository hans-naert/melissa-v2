import argparse
import json

from stt import console_stt, stt
from tts import console_tts, tts
# import the logic function from logic.py
from logic import logic

parser = argparse.ArgumentParser(description="Run Melissa with console or voice I/O.")
parser.add_argument(
    "--mode",
    choices=("type", "speak"),
    help="I/O mode: type for console input/output, speak for microphone/audio.",
)
args = parser.parse_args()
input_mode = args.mode

if input_mode == "type":
    get_user_input = console_stt
    output_response = console_tts
else:
    get_user_input = stt
    output_response = tts

# Load the profile.json file
with open("profile.json") as f:
    profile = json.load(f)

name = profile["name"]

# Pass the name to the logic function
llm_response = logic(f"Hello, my name is {name}")

# Pass the response from the logic function to the selected output
output_response(llm_response)

while True:
    try:
        userInput = get_user_input()

        # Check if user input is empty or None
        if not userInput:
            print("No input detected. Ending conversation...")
            break

        # Process user input and respond
        output_response(logic(userInput))

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        break
