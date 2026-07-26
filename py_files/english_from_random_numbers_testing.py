import subprocess
import time
from wordsegment import load, segment
import os
start_time = time.perf_counter()

print("Loading...")

load()

with open("/usr/share/dict/words") as f:
    dictionary = set(word.strip().lower() for word in f)

with open("/Users/eduan/work/testing/random_text", "r") as file:
    random_text = file.read()


detected_words = segment(random_text)


real_words = [
    word for word in detected_words
    if word.lower() in dictionary
]
longest_word = max(real_words, key=len)
longest_word_len = len(longest_word)
word_count = len(real_words)


print("\a Loaded!")

time.sleep(1)

print()
print(f"{word_count} words were found:")
print()
print(real_words)
print()
print(f"Longest word: '{longest_word}', at {longest_word_len} characters.")

end_time = time.perf_counter()

time_passed = (end_time - start_time) - 1.5
print(f"Finding these words took approximately {time_passed:.6f} seconds.")