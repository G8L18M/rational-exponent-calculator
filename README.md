This project uses a new approximation method to compute the value of T^(N/R).
Here, T is an integer, and N and R are integers denoting the numerator and denominator of the exponent, respectively.

Use main.py to test out the algorithm:

1. Run the program
2. On the first line, input the value of T.
3. On the second line, input N and R, separated by a space.
4. On the third line, input a nonnegative integer number of iterations of Halley's method. Increasing this number will increase the accuracy of the result.
5. On the fourth line, input a nonnegative integer number of digits after the decimal point in the result. Note that due to floating-point arithmetic, the program loses accuracy if too many digits are requested.

Use experiments.py to compare the Digit-Based Method against the Built-In Method, the Constant Guess of 1.0 with Halley's Method, and the Exponential Shortcut.

The inputs can be edited in input.csv, and the outputs are shown in output.json.

The analyses of the results, which include the average runtime and average number of iterations for each method, can be computed using analyses.py and viewed in analyses.txt.