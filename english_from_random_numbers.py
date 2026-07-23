import subprocess
import time
from wordsegment import load, segment
start_time = time.perf_counter()

print("Loading...")

load()

with open("/usr/share/dict/words") as f:
    dictionary = set(word.strip().lower() for word in f)

character_count = 100000
command = f"LC_CTYPE=C tr -dc 'a-z' < /dev/urandom | head -c {character_count}"

result = subprocess.run(command, shell=True, capture_output=True, text=True)
random_text = result.stdout


detected_words = segment(random_text)


real_words = [
    word for word in detected_words
    if word.lower() in dictionary
]
longest_word = max(real_words, key=len)
longest_word_len = len(longest_word)
word_count = len(real_words)

print("Loaded!")

time.sleep(1.5)

print()
print(f"Dictionary words found:")
print()
print(real_words)
print()
print(f"Longest word: '{longest_word}', at {longest_word_len} characters.")

end_time = time.perf_counter()

time_passed = (end_time - start_time) - 1.5
print(f"Finding these words took approximately {time_passed:.2f} seconds.")