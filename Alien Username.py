# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    s = input()

    ok = re.match(r"^[_\.]\d+[a-z]*_?$", s, re.I)

    print("VALID" if ok else "INVALID")
