#!/usr/bin/env python3
import sys

i = 0
for line in sys.stdin:
    print(i, line)
    i += 1
print("--- END ---") 
