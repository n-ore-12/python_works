import time
N=10
print("filloi")

for i in range(N):
    print(f"{100*(i+1)/N : .2f}%", end="\r", flush=True)
    time.sleep(0.5)

print("\nmbraroi")