import sys

def calc(num):
    return ((2 * num) - 2)

argv = sys.argv
target = float(argv[1])
rate = float(argv[2])
cnt = 0
while True:
    cnt = cnt+1
    x = calc(target)
    y = target - (x * rate)
    if y < 1.0001:
        break
    target = y
    print(y)

print(cnt)


