# minimal space utilization.
#  he used his unique but complex way of representation for tracking the gems, as follows:
# For each gem, the count is maintained and displayed against each gem (except count 1).
# For each Box, if the gems proportionate quantity is the multiple of a number, then that is displayed after the box closes.

# In the kingdom of K king, there are 5 unique sized Jewel Boxes represented as (Biggest) $, %, &, # and * (Smallest) with closing lids as ; : , . and + respectively. E
# Each of the jewel boxes contains gems numbered as A, B, C, D… Z. 

# Sample Input 2:
# $A4%BC&XB3,2:3;

# Sample Output 2:
# A4B21C3X6

# Now, you need to simplify and count the total number of unique treasures and show them in output in sorted order (according to gems).

def jewelBox():
    inp = input()

    # store the input in a diffrents list for diffrent boxes

    Dollar = []
    Percent = []
    And = []
    Hash = []
    Star = []

    # store the input in a diffrents list for diffrent boxes
    for i in inp:
        if i == "$":
            Dollar.append(i)
        elif i == "%":
            Percent.append(i)
        elif i == "&":
            And.append(i)
        elif i == "#":
            Hash.append(i)
        elif i == "*":
            Star.append(i)
        else:
            pass
    
    # store the gems of diffrent boxes in a their respective boxes list
    Dollar.append(inp[inp.index("$")+1:inp.index("%")])
    Percent.append(inp[inp.index("%")+1:inp.index("&")])
    And.append(inp[inp.index("&")+1:inp.index("#")])
    Hash.append(inp[inp.index("#")+1:inp.index("*")])
    Star.append(inp[inp.index("*")+1:inp.index(";")])


    print(Dollar)
    print(Percent)
    print(And)
    print(Hash)
    print(Star)



if __name__ == "__main__":
    jewelBox()
            

    
if __name__ == "__main__":
    jewelBox()
