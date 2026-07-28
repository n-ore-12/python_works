import random
import time
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(123)

def die_roll_1(trials):
    statistics = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(trials):
        roll = random.randint(1,6)
        statistics[roll] += 1
    total_roll = sum([k * v for k,v in statistics.items()]) 
    average_roll = total_roll / trials
    return average_roll, statistics.items()

trials = 10000
N_exp = 10000
avg_exp = []
T = []
for i in range(N_exp):
    start = time.perf_counter()
    avg, _ = die_roll_1(trials)
    avg_exp.append(avg)
    T.append(time.perf_counter() - start)



def die_roll_2(trials):
    die = np.array([1,2,3,4,5,6])
    counts = np.zeros(6)
    rolls = rng.integers(low=1, high=6, size=trials, endpoint=True)
    sum = np.sum(rolls)
    avg = sum / trials
    for i in range(6):
        counts[i] = len(rolls[rolls==die[i]])/trials
    return avg, counts



trials = 10000
N_exp = 10000
avg_exp1 = np.zeros(N_exp)
T1 = np.zeros(N_exp)

for i in range(N_exp):
    start = time.perf_counter()
    avg_exp1[i], _ = die_roll_2(trials)
    T1[i] = time.perf_counter() - start


hist_avg, bin_avg = np.histogram(avg_exp1, bins=50)

plt.figure()
plt.plot(avg_exp1, 'ok')
plt.axhline(y=3.5, linestyle = "dashed")
plt.title("Averages using Numpy arrays")


plt.figure()
plt.plot(T1,'ok', label="Numpy algorithm")
plt.plot(T, 'or', label="Traditional dictionary algorithm")
plt.legend()


plt.figure()
plt.plot(bin_avg[:-1], hist_avg,'-k',lw=2,ds="steps-mid",)

plt.figure()
plt.hist(T1)
plt.yscale('log')
plt.title("Numpy algorithm")

plt.figure()
plt.title("Traditional dictionary algorithm")
plt.yscale("log")
plt.hist(T)


plt.figure()
plt.plot(avg_exp, 'ok')
plt.axhline(y=3.5, linestyle="dashed")
plt.title("Averages using Dictionaries")

plt.show()

