#!/usr/bin/env python3

cels_temp = input("Enter temperature in Celsius: ")
cels_temp = float(cels_temp)
fah_temp = (cels_temp * 9/5) + 32
print(f'{cels_temp}C is equivalent to {fah_temp}F.')
