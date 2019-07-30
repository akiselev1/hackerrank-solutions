"""

 Created by akiselev on 2019-07-15
 
 CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F.
■ A-F letters can be lower case. (a-f are also valid digits).

Examples

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff

You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}

"""
import re
n = int(input())
color_regex = re.compile(r'#[A-Fa-f0-9]{3,6}')
for _ in range(n):
    line = input()
    if re.match(color_regex, line):
        continue
    else:
        for m in re.findall(color_regex, line):
            print (m)
