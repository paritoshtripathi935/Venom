# Chef has a rectangular plate of length N cmNcm and width M cmMcm. He wants to make a wireframe around the plate. The wireframe costs XX rupees per cm.
# Determine the cost Chef needs to incur to buy the wireframe.
# Input
"""
3
10 10 10
23 3 12
1000 1000 1000
"""

# start of code
def wireframe():
    n = int(input())
    if n <= 100 or n >= 1:
        for i in range(n):
            length, width, cost = map(int, input().split())
            if length <= 1000 or width <= 1000 or cost <= 1000:
                print(2*(length+width)*cost)

if __name__ == "__main__":
    # pass in the list of words as input in shortstring
    wireframe()
    