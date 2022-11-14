# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

html = ''.join([input() for _ in range(int(input()))])

find_href = r'<a\s+href="(.*?)".*?>(.*?)</a>'
remove_tags = r'</?(\w+).*?>'
match = re.findall(find_href, html, re.I)
if bool(match):
    for link, title in match:
        title = re.sub(remove_tags, "", title)
        print(link + ',' + title.strip())
