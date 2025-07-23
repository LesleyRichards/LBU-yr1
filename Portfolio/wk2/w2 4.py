#!/usr/bin/env python3

sweets = input("Enter the amount of sweets: ")
pupils = input("Enter the amount of students that attended ")
sweets = int(sweets)
pupils = int(pupils)
sweets_per = sweets // pupils
left_over = sweets % pupils
print(f"Each student will get {sweets_per} sweets, and there will be {left_over} sweets left over.")
