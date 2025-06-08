import math
from decimal import *

T = Decimal(input())
N, R = list(map(int, input().split()))
n = int(input())
decimalPlaces = int(input())

getcontext().prec = int(decimalPlaces * 1.5 + 5)

isNegative = False

if R == 0:
    print("Error: cannot divide by 0")
    exit()

if N / R < 0:
    isNegative = True
    N = abs(N)
    R = abs(R)

if N < 0 and R < 0:
    N = abs(N)
    R = abs(R)

if T == 0:
    print(0)
elif T == 1:
    print(1)
elif T < 0 and R % 2 == 0:
    print("Error: cannot take an even root of a negative number")
elif (N / R) == int(N / R):
    print(T ** (N // R))
else:
    D = int(math.ceil(math.log(2, abs(T))))
    
    L_X = Decimal(1 << (R * ((D - 1) // R)))
    L_Y = Decimal(1 << ((D - 1) // R))
    U_X = Decimal(1 << (R * ((D + R - 1) // R)))
    U_Y = Decimal(1 << ((D + R - 1) // R))

    A = (T / abs(T)) * (L_Y + ((abs(T) - L_X) / (U_X - L_X)) * (U_Y - L_Y))
    for i in range(n):
        A_new = A - (2 * (A ** (R + 1)) - 2 * T * A) / (R * (A ** R) + A ** R + T * R - T)
        if A == A_new:
            break
        else:
            A = A_new
    T_r = A

    if isNegative:
        ans = 1 / ((T_r) ** N)
    else:
        ans = T_r ** N

    formatting = '{:.' + str(decimalPlaces) + 'f}'
    print(formatting.format(ans))
