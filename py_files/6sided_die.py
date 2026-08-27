import random
import time
import matplotlib.pyplot as plt


def die_roll_1(trials):
    statistics = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(trials):
        roll = random.randint(1,6)
        statistics[roll] += 1
    total_roll = sum([k * v for k,v in statistics.items()]) 
    average_roll = total_roll / trials
    return average_roll, statistics.items

trials = 10000
N_exp = 10000
avg_experiment = []
T = []
for i in range(N_exp):
    start = time.perf_counter()
    avg_experiment(i) = avg_experiment.append(die_roll_1(trials))
    T(i) = time.perf_counter() - start




print("rolling", end="", flush=True)
for k in range(4):
    time.sleep(1)
    print(".", end="", flush=True)

print(f"\nStatistics of a 6-sided die after {trials} rolls")
print(statistics)
print(f"Average Roll: {average_roll}")

plt.bar(statistics.keys(), statistics.values(), color = "b")



plt.title(r"Statistics of a 6-sided die after %d rolls - $\rm \mu$: %.2f"%(trials, average_roll))

plt.xlabel("Face")
plt.ylabel("Rolls")
plt.axvline(x=average_roll,linewidth=2, linestyle ="dashed", color="r", label= "Average Roll")
plt.legend()
plt.show()