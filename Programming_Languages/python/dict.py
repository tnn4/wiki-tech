# minimum deletions to make character frequencies unique, 
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# check if dict values are unique
# How to create key or append an element to key?
from collections import defaultdict
import sys
# regular expression
import re
"""
( ^[ ) : means match anything but
e.g. ^[<>]
[^a-z]
"""


char_set="abcdefghijklmnopqrstuvwxyz"
test_string="sjfjsjfjsdjdsjkeruthjghbncvqqwwtrrtuitopphfnmbnbmnzxxcvvbbnnmkassdfghhjklqwerrtyuiiopcnmcvasfjzzzz"
bad_string="jsdjflsjf5afdjkjglksd"
# this is a string literal but we can exapt it as a multiline comment
"""
    https://blog.logrocket.com/understanding-type-annotation-python/
    float: float values, such as 3.10
    int: integers, such as 3, 7
    str: strings, such as 'hello'
    bool: boolean value, which can be True or False
    bytes: represents byte values, such as b'hello'

"""

class GoodString:
    # constructor
    def __init__(self, test_string):
        self.test_string=test_string
    #fin

    # a string is 'good' when it has unique frequencies for every letter/(element in character set)
    def is_string_good() -> bool:
        pass
    #fin

    def is_string_len_valid(self) -> bool:
        if 1 < len(self.test_string) < 1e5:
            return True
        #fi
        return False
    #fin

    def contains_invalid_characters(self) -> bool:
        if re.search('[^a-z]', self.test_string) != None:
            print('invalid characters detected')
            return False
        #fi
        print('string contains valid characters')
        return True
    #fin

#ass

def string_not_longer_than(string:str, max: int) -> bool:
    if len(string) > max:
        return False
    else:
        return True
    #fi
#fin

# a string is complete if it uses the entire character set
def is_complete(string: str) -> bool:
    d = defaultdict(list)
    
    for c in string:
        if c not in string:
            d.setdefault(c,0)
        else:
            print(type(d[c]))
            d[c]+=1
        #fi
    #end_for

    for k,v in d:
        if d[k] == 0:
            return False
        #fi
    #end_for

    return True
#fin

def main():
    print("how to create key or append element to key?")
    #s = [('a',0), ('b',0)]
    d = defaultdict(list)
    #for k,v in s:
    #    d[k].append(v)
    print("len of test_string: ", len(test_string))
    
    for c in test_string:
        if c not in d:
             d.setdefault(c,0)
        else:
            #print(type(d[c]))
            d[c]+=1
        #fi
    #end_for

    print(d)
    print("-- SORTED: --")
    print(sorted(d))
    #print(is_complete(test_string))

    gs = GoodString(test_string=test_string)
    gs.contains_invalid_characters()

    gs2 = GoodString(test_string=char_set)
    gs2.contains_invalid_characters()

    gs3=GoodString(test_string=bad_string)
    gs3.contains_invalid_characters()

    result = re.search('^[a-z]',test_string)
    print("search result: ", result)
#fin

if __name__ == "__main__":
    sys.exit(main())
#fi

# How can I iterate over every characte rin a given encoding using Python?