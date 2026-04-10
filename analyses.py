import json

methods = ["Digit-Based Method", "Built-In Method", "Constant Initial Guess of 1.0", "Exponential Shortcut"]
tests = 1050

total_iterations = [0, 0, 0, 0]
total_runtime = [0, 0, 0, 0]

results = []

with open("output.json") as file:
    results = json.load(file)

for result in results:
    for i in range(4):
        total_iterations[i] += result[methods[i]]["Iterations"]
        total_runtime[i] += result[methods[i]]["Runtime (ns)"]

avg_iterations = [0.0, 0.0, 0.0, 0.0]
avg_runtime = [0.0, 0.0, 0.0, 0.0]

for i in range(4):
    avg_iterations[i] = total_iterations[i] / tests
    avg_runtime[i] = total_runtime[i] / tests

with open("analyses.txt", "w") as f:
    for i in range(4):
        print(methods[i], file=f)
        print("Average Iterations: " + str(avg_iterations[i]), file=f)
        print("Average Runtime (ns): " + str(avg_runtime[i]), file=f)
        print("", file=f)