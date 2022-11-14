Regex_Pattern = r"(\S\S\s){2}\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())