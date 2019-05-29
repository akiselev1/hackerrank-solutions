"""

 Created by akiselev on 2019-05-20
 
 
"""

import re


if __name__ == '__main__':
    n = int(input())
    bin_str="{0:0b}".format(n)
    #print(bin_str)
    get_num_ones = re.findall(r"1+", bin_str)
    print(len(max(get_num_ones, key=len)))