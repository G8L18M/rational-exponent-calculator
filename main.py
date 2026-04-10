import math

T = int(input())
N, R = list(map(int, input().split()))
decimalPlaces = 10

isNegative = False

if R == 0:
    print("Error: cannot divide by 0")
    exit()

isNegative = True if (N / R < 0) else False

N = abs(N)
R = abs(R)

if T == 0:
    print(0)
elif T == 1:
    print(1)
elif T < 0 and R % 2 == 0:
    print("Error: cannot take an even root of a negative number")
elif N % R == 0:
    sign = 1
    if T < 0:
        sign = -1
        T = abs(T)
    result = T ** (N // R)
    if (sign == -1) and (N % 2 == 1):
        result = -result
    print(result)
else:
    D = int(math.ceil(math.log(abs(T), 2)))
    
    L_X = 1 << (R * ((D - 1) // R))
    L_Y = 1 << ((D - 1) // R)
    U_X = 1 << (R * ((D + R - 1) // R))
    U_Y = 1 << ((D + R - 1) // R)

    A = (T / abs(T)) * (L_Y + ((abs(T) - L_X) / (U_X - L_X)) * (U_Y - L_Y))
    
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
    T_r = A

    if isNegative:
        ans = 1 / (T_r ** N)
    else:
        ans = T_r ** N

    formatting = '{:.' + str(decimalPlaces) + 'f}'
    print(formatting.format(ans))