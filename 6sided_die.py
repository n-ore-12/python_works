import random
import time

statistics = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
trials = 100

for i in range(trials):
    roll = random.randint(1,6)
    statistics[roll] += 1

total_roll = sum([k * v for k,v in statistics.items()]) 

average_roll = total_roll / trials

print("rolling", end="", flush=True)
for k in range(4):
    time.sleep(1)
    print(".", end="", flush=True)
print()

print(f"Statistics of a 6-sided die after {trials} rolls")
print(statistics)
print(f"Average Roll: {average_roll}")

