# given a string s contaning just the characters '(', ')' ,'[' ,']' ,'{' ,'}' determine if the input string is valid 
 
import time

start_1 = time.time()
def is_valid(s):
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':            # if the current character is an opening bracket, push it to the stack
            stack.append(i)                             
        elif i == ')':                                 # if the current character is a closing bracket, check if the stack is empty
            if len(stack) == 0 or stack.pop() != '(':  # if the current character is a closing bracket, 
                return False                           # and the stack is empty or the top of the stack is not a matching opening bracket, return False

        elif i == ']':                                 # if the current character is a closing bracket, 
            if len(stack) == 0 or stack.pop() != '[':  # and the stack is empty or the top of the stack is not a matching opening bracket, return False 
                return False
        
        elif i == '}':                                  # if the current character is a closing bracket, 
            if len(stack) == 0 or stack.pop() != '{':   # and the stack is empty or the top of the stack is not a matching opening bracket, return False
                return False        
    return len(stack) == 0

print(is_valid('{[{(({}))]}}'))
end_1 = time.time()
print("Total Time", end_1 - start_1)
#print(is_valid('()[]{}'))

# given a string s contaning just the characters '(', ')' ,'[' ,']' ,'{' ,'}' determine if the input string is valid using dictionary
start_2 = time.time()
def is_valid_dictionary(s):
    d = {')':'(', ']':'[', '}':'{'}  # create a dictionary with the closing bracket as the key and the opening bracket as the value
    stack = []                       # create an empty stack to hold the opening brackets 
    for i in s:                      # loop through the string 
        if i in d:                   # if the current character is in the dictionary, push it to the stack 
            if len(stack) == 0 or stack.pop() != d[i]:  # if the current character is in the dictionary, 
                                                        # and the stack is empty or the top of the stack is not a matching opening bracket, return False
                return False
        else:
            stack.append(i)          # if the current character is not in the dictionary, push it to the stack 
    return len(stack) == 0           # if the stack is empty, return True

print(is_valid_dictionary('{[{(({}))]}}'))
end_2 = time.time()
print("Total Time", end_2 - start_2)
#print(is_valid_dictionary('()[]{}'))

