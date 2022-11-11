"""
Suppose you are given a set of N disks. You would like to arrange these disks in stacks in such a way that the disks in a single stack must be ordered by
their radii in a strictly increasing order with the top-most disk have the smallest radius. For example, a stack of radii (4,3,2) is valid, while (4,2,3) is invalid.
The algorithm is as follows:
1. First, you initiate an empty set of stacks.

Then, you process the disk in the chosen order using following pattern:
1. If there is at least one stack such that you can put the current disk on the top of the stack without making it invalid.
2. Otherwise, you make a new stack containing only the current disk.
"""

def disk_stack(disk_list):
    stack_list = []
    for disk in disk_list:
        for stack in stack_list:
            if disk < stack[-1]: # if disk is smaller than the top of the stack
                stack.append(disk) # append the disk to the stack
                break
        else:
            stack_list.append([disk])
    return stack_list

if __name__ == '__main__':
    disk_list = [8,7,6,5,4,3,2,1]
    stack = disk_stack(disk_list)
    print(stack)
    print(len(stack))
    for i in stack:
        # if stack second element is not empty
        if i[1:]:
            print(i[-1])
        else:
            print(i[0])
