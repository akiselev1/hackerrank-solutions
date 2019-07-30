"""

 Created by akiselev on 2019-06-18
 
A valid postal code P have to fullfil both below requirements:

P must be a number in the range from 100000 to 999999 inclusive.
P must not contain more than one alternating repetitive digit pair.

RE lookaround tutorial: https://www.regular-expressions.info/lookaround.html
"""

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.
#regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)