#!/usr/bin/env python3

students = input("How many students? ")
group_size = input("Required group size? ")
students = int(students)
group_size = int(group_size)
groups = students // group_size
leftovers = students % group_size
print(f'There will be {groups} groups with {leftovers} students left over')