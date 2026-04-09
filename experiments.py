import csv
import json
import time
import math

def benchmark(T, N, R, decimal_places=10, runs=1000):
    formatting = '{:.' + str(decimal_places) + 'f}'
    results = []

    start = time.perf_counter_ns()
    for _ in range(runs):
        ans, iterations = digit_based(T, N, R)
    end = time.perf_counter_ns()

    results.append([formatting.format(ans), iterations, (end - start) / runs])

    start2 = time.perf_counter_ns()
    for _ in range(runs):
        ans2, iterations2 = builtin(T, N, R)
    end2 = time.perf_counter_ns()

    results.append([formatting.format(ans2), iterations2, (end2 - start2) / runs])

    start3 = time.perf_counter_ns()
    for _ in range(runs):
        ans3, iterations3 = constantGuess(T, N, R)
    end3 = time.perf_counter_ns()

    results.append([formatting.format(ans3), iterations3, (end3 - start3) / runs])

    start4 = time.perf_counter_ns()
    for _ in range(runs):
        ans4, iterations4 = exponentialShortcut(T, N, R)
    end4 = time.perf_counter_ns()

    results.append([formatting.format(ans4), iterations4, (end4 - start4) / runs])

    return results

def digit_based(T, N, R):
    isNegative = True if (N / R < 0) else False

    N = abs(N)
    R = abs(R)

    ans = 0
    iterations = 0

    if T == 0:
        ans = 0
    elif T == 1:
        ans = 1
    elif R == 1:
        if isNegative:
            return builtin(T, -N, R)
        else:
            return builtin(T, N, R)
    else:
        D = int(math.ceil(math.log(abs(T), 2)))
        
        L_X = 1 << (R * ((D - 1) // R))
        L_Y = 1 << ((D - 1) // R)
        U_X = 1 << (R * ((D + R - 1) // R))
        U_Y = 1 << ((D + R - 1) // R)

        A = (T / abs(T)) * (L_Y + ((abs(T) - L_X) / (U_X - L_X)) * (U_Y - L_Y))
        
        T_r, iterations = halley(T, R, A)

        if isNegative:
            ans = 1 / (T_r ** N)
        else:
            ans = T_r ** N
    
    return ans, iterations

def builtin(T, N, R):
    sign = 1
    if T < 0:
        sign = -1
        T = abs(T)
    result = (T ** (1 / R)) ** N
    if (sign == -1) and (N % 2 == 1):
        result = -result
    return result, 0

def constantGuess(T, N, R):
    isNegative = True if (N / R < 0) else False

    N = abs(N)
    R = abs(R)

    ans = 0
    iterations = 0

    if T == 0:
        ans = 0
    elif T == 1:
        ans = 1
    elif R == 1:
        if isNegative:
            return builtin(T, -N, R)
        else:
            return builtin(T, N, R)
    else:
        A = 1.0
        T_r, iterations = halley(T, R, A)

        if isNegative:
            ans = 1 / (T_r ** N)
        else:
            ans = T_r ** N
    
    return ans, iterations

def exponentialShortcut(T, N, R):
    isNegative = True if (N / R < 0) else False

    N = abs(N)
    R = abs(R)

    ans = 0
    iterations = 0

    if T == 0:
        ans = 0
    elif T == 1:
        ans = 1
    elif R == 1:
        if isNegative:
            return builtin(T, -N, R)
        else:
            return builtin(T, N, R)
    else:
        A = (T / abs(T)) * (2 ** (math.log(abs(T), 2) / R))
        T_r, iterations = halley(T, R, A)

        if isNegative:
            ans = 1 / (T_r ** N)
        else:
            ans = T_r ** N
    
    return ans, iterations

def halley(T, R, A):
    iterations = 0
    while True:
        if abs(R * (A ** R) + A ** R + T * R - T) < 1e-14:
            break
        A_new = A - (2 * (A ** (R + 1)) - 2 * T * A) / (R * (A ** R) + A ** R + T * R - T)
        if abs(A - A_new) < 1e-12:
            break
        elif iterations == 100:
            break    
        else:
            A = A_new
            iterations += 1
    return A, iterations

methods = ["Digit-Based Method", "Built-In Method", "Constant Initial Guess of 1.0", "Exponential Shortcut"]

input = []
with open("input.csv") as file:
    heading = next(file)
    reader = csv.reader(file)
    for row in reader:
        input.append(row)

output = []

for row in input:
    T = int(row[0])
    N = int(row[1])
    R = int(row[2])
    result = benchmark(T, N, R)

    test = {}
    test["T"] = T
    test["N"] = N
    test["R"] = R
    for i in range(4):
        test[methods[i]] = {}
        test[methods[i]]["Output"] = result[i][0]
        test[methods[i]]["Iterations"] = result[i][1]
        test[methods[i]]["Runtime (ns)"] = result[i][2]
    
    output.append(test)

with open("output.json", "w") as file:
    json.dump(output, file, indent=2)