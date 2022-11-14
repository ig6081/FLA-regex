Regex_Pattern = r'^(Mr|Ms|Mrs|Dr|Er)\.[a-zA-Z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())