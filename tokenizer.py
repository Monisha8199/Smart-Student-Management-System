from pathlib import Path

# Locate the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Locate text.txt
text_file = BASE_DIR / "data" / "text.txt"

# Read the file
with open(text_file, "r", encoding="utf-8") as file:
    text = file.read().lower()

print("===== Original Text =====")
print(text)

# Split into words
tokens = text.split()

print("\n===== Tokens =====")
print(tokens)

# Build vocabulary
vocab = sorted(set(tokens))

print("\n===== Vocabulary =====")
print(vocab)

# Assign IDs
word_to_id = {word: idx for idx, word in enumerate(vocab)}

print("\n===== Word to ID =====")
print(word_to_id)

# Convert words to IDs
encoded = [word_to_id[word] for word in tokens]

print("\n===== Encoded Text =====")
print(encoded)