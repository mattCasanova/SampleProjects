#!/usr/local/bin/python3

#simple fibonacci series
# the sum of the two elements defines the next set

a, b = 0, 1;
while b < 50:
    print(b);
    a, b = b, a + b;
