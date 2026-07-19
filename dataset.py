from pathlib import Path

# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Read the text
text_file = BASE_DIR / "data" / "text.txt"

with open(text_file, "r", encoding="utf-8") as file:
    text = file.read().lower()

# Split into words
tokens = text.split()

print("Total Tokens:", len(tokens))

sequence_length = 5

print("\nTraining Samples:\n")

for i in range(len(tokens) - sequence_length):

    input_sequence = tokens[i:i + sequence_length]

    target_word = tokens[i + sequence_length]

    print("Input :", input_sequence)
    print("Target:", target_word)
    print("-------------------------")