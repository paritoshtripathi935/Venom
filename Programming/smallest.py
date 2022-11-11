"""
Determine the smallest possible size for a new folder to allow the creation of balanced folders. Return -1 if creating a
balanced folders are not possible
Complete the function smallestSize with the following parameters:

input
5
14 11 7 13 12
1,2,1,3,1,4,4,5
"""

import math
import os
import random
import re

# find the smallest size of a folder that can be created to allow the creation of balanced folders of size k or less
def smallestSize(k, arr, edges):
    # Write your code here
    # create a graph
    graph = {}
    for i in range(len(arr)):
        graph[i+1] = [arr[i], []]
    for i in range(0, len(edges), 2):
        graph[edges[i]][1].append(edges[i+1])
        graph[edges[i+1]][1].append(edges[i])
    # print(graph)
    # find the max size of a folder
    max_size = 0
    for i in graph:
        max_size = max(max_size, graph[i][0])
    # print(max_size)
    # find the smallest size of a folder
    for i in range(max_size, sum(arr)+1):
        if is_balanced(graph, i, k):
            return i
    return -1

def is_balanced(graph, size, k):
    visited = set()
    for i in graph:
        if i not in visited:
            if not dfs(graph, i, size, k, visited):
                return False
    return True

def dfs(graph, node, size, k, visited):
    visited.add(node)
    if graph[node][0] > size:
        return False
    if len(graph[node][1]) == 0:
        return True
    count = 0
    for i in graph[node][1]:
        if i not in visited:
            if dfs(graph, i, size, k, visited):
                count += 1
    return count <= k

if __name__ == '__main__':
    m = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    edges = list(map(int, input().rstrip().split()))
    result = smallestSize(m, arr, edges)
    print(result)
    
