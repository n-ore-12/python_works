import numpy as np
import time
import matplotlib.pyplot as plt

rng = np.random.default_rng(123)

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
avg_exp = np.zeros(N_exp)
T = np.zeros(N_exp)

for i in range(N_exp):
    start = time.perf_counter()
    avg_exp[i], _ = die_roll_2(trials)
    T[i] = time.perf_counter() - start


hist_avg, bin_avg = np.histogram(avg_exp, bins=50)

plt.figure()
plt.plot(avg_exp, 'ok')
plt.axhline(y=3.5, linestyle = "dashed")

plt.figure()
plt.plot(T,'ok')

plt.figure()
plt.plot(bin_avg[:-1], hist_avg,'-k',lw=2,ds="steps-mid")

plt.figure()
plt.hist(T)
plt.yscale('log')

plt.show()