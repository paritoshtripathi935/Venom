
"""
Given a binary array arr[ ] of size n. The array contains only 0 and 1.
You can perform the following operation atmost once:
Select any subarray from the given array and flip all its elements i.e. change 0 to 1
and 1 to 0.

After the operation, find the length of the largest subarray containing all 1s.

Input :
n = 4
arr = {0, 1, 1, 0}
Output :
3

Explanation :
The optimal way is to choose subarray
arr[0:0] that is {0} and flip it to 1
so finally array becomes {1, 1, 1, 0}.
So the answer is 3.

Input :
n = 5
arr = {1, 0, 0, 0, 1}
Output :
5

Possibly your code doesn't work correctly for multiple test-cases (TCs).
The first test case where your code failed:
Input:

6
0 0 1 1 0 1

And Your Code's output is:
5


Its Correct output is:
4

"""


"""
class Solution {
    public static int toggle(int n, int[] arr) {
        int s = 0,current = 0;
        int max = 0;
        int c = 0;
        // sliding window comncept
        while(current<arr.length){
            if(arr[current]==1){
                c++;
                max = Math.max(max,c);
                current++;
            }
            else{
            while(current<arr.length&&arr[current]==0){
                c++;
                current++;
                max = Math.max(max,c);
            }
            s = current;
            while(current<arr.length&&arr[current]==1){
                c++;
                current++;
               max = Math.max(max,c);
            }
            current=s;
            c=0;
            }
    }
    return max;
}
}
"""
import sys
def max_len_subarray(arr, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        max_len = 0
        s = 0
        current = 0
        c = 0
        while current < n:
            if arr[current] == 1:
                c += 1
                max_len = max(max_len, c)
                current += 1
            else:
                while current < n and arr[current] == 0:
                    c += 1
                    current += 1
                    max_len = max(max_len, c)
                s = current
                while current < n and arr[current] == 1:
                    c += 1
                    current += 1
                    max_len = max(max_len, c)
                current = s
                c = 0
        return max_len

# completxity: O(n)
# space: O(1)
# wrtie merge sort and quick sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_len_subarray(arr, n))

if __name__ == "__main__":
    main()