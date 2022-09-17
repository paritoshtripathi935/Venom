import math

def build_tree(arr, tree, start, end, node):
    if start == end: # leaf node 
        tree[node] = arr[start]
        return
    mid = (start + end) // 2                        # mid point of the array to store in the left and right subtree
    build_tree(arr, tree, start, mid, 2*node)       # left subtree and passing the left child of the node
    build_tree(arr, tree, mid+1, end, 2*node+1)     # right subtree and passing the right child of the node
    tree[node] = min(tree[2*node], tree[2*node+1])  # storing minmum value in the root node of the tree

                                                    # here we are making tree of size 4*n because we are using 1 based indexing 
                                                    # and we are using 2*node and 2*node+1 for left and right subtree respectively
def query(tree, start, end, node, l, r):
    if start > r or end < l:                        # if the range is completely outside the given range
        return math.inf
    if start >= l and end <= r:                     # if the range is completely inside the given range
        return tree[node]
    mid = (start + end) // 2                        # mid point of the array
    left = query(tree, start, mid, 2*node, l, r)    # left subtree
    right = query(tree, mid+1, end, 2*node+1, l, r) 
    return min(left, right)                         # and here we returning the minimum value between the range l and r

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0]*(4*n)                                # tree of size 4*n
    build_tree(arr, tree, 0, n-1, 1)                # building the tree
    l, r = map(int, input().split())                # range of the query, l and r are inclusive 
    print(query(tree, 0, n-1, 1, l, r))             # calling the query function and passing the tree, start, end, node, l and r

if __name__ == "__main__":
    main()

# explane above code
# here we are using segment tree to solve this problem
# we are using 1 based indexing for tree
# we are using 2*node and 2*node+1 for left and right subtree respectively
# we are using math.inf for infinity
# we are using min(left, right) for returning the minimum value between the range l and r

# time complexity of this code is O(logn)
# space complexity of this code is O(n)