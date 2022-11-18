"""
Your mother's birthday is coming this weekend. You want to buy a necklace to gift her on her birthday. You want to use
Gold(G) and Diamond(D) to make a necklace. Both have some level of density. Your mother likes ornaments of X density.
You first mix one gram of gold to make a necklace and then one gram of Diamond alternatively. The density of the ornament
is an average of the densities of the mixed elements. You want to achieve a density as close as possible to X. How many
grams of gold and diamond should be mixed so that the density of the omament is as close as to X?

Note: If there are multiple solutions, print the smallest one.
Complete the function goldDiamondNecklace with the parameters:
an integer G representing the density of gold
an integer D representing the density of diamond
an integer X representing the Desired density of ornament

Function should return:
a single positive integer denoting the minimum number of grams of gold and diamond required to be mixed to get as close
as to the desired density X

"""
import math

def goldDiamondNecklace(G, D, X):
    # Write your code here
    if G == D:
        return 1
    if G > D:
        G, D = D, G
    if X > D:
        return 1
    if X < G:
        return 1
    if X == G:
        return 1
    if X == D:
        return 1
    if X == (G + D) / 2:
        return 1
    if X < (G + D) / 2:
        return math.ceil((D - X) / (X - G))
    if X > (G + D) / 2:
        return math.ceil((X - G) / (D - X))

if __name__ == '__main__':
    G = int(input().strip())

    D = int(input().strip())

    X = int(input().strip())

    result = goldDiamondNecklace(G, D, X)