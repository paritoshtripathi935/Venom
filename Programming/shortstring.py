def shortstring():
    n = int(input())
    if n <= 100 or n >=1:
        for i in range(n):
            word = input()
            if len(word) > 10: # if word is longer than 10 characters
                print(word[0] + str(len(word)-2) + word[-1])  # print first letter, number of characters between first and last letter, and last letter
            else:
                print(word) # if word is less than 10 characters, print word

if __name__ == "__main__":
    # pass in the list of words as input in shortstring
    shortstring()

# time complexity: O(n) where n is the number of words
# space complexity: O(1) since the number of variables is constant


