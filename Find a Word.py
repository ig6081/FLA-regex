# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = " ".join(input() for _ in range(int(input())))

for _ in range(int(input())):
    w = input()
    print(len(re.findall(r"(^|(?<=\W))" + w + r"(?=\W)", s, re.I)))
