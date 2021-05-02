import sys
import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n+1):
        line = input()
x = re.findall("#[^\s]+\s", line)
print(x)
