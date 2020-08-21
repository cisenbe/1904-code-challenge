#!/usr/bin/python3
import sys
from itertools import permutations

def main():
    # Wrap this in a print() so it functions properly and works with the tests
    print(next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    
    # This is only needed to pass the unit test; sys.argv[1] is always a string
    numStr = str(num)
    
    strList = list(numStr)
    # Create an object containing all permutations of our character list
    permObj = permutations(strList)
    
    # Join our tuples together as strings, and then cast them as integers
    intList = [int(''.join(f)) for f in permObj]
    intList.sort(reverse = True)
    
    # Find the index of our input. If it's first, we can't get any bigger
    if intList.index(int(num)) == 0:
        return -1
    # Otherwise, our next-largest permutation is one index back
    else:
        return intList[intList.index(int(num))-1]

if __name__ == "__main__":
    main()



