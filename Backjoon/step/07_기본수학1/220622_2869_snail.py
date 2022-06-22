import sys

a, b, v = map(int, sys.stdin.readline().split())

print(((v-b) // (a-b)) + 1 if (v-b) % (a-b) > 0 else (v-b)//(a-b))