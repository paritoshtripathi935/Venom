"""
The emperor listed K most used irrelevant keywords. The emperor approached you (a software engineer) to write a program that takes this list of irrelevant keywords. Along with this he is ready to give the n different opinions that he received from his representatives. You need to identify the most irrelevant opinion.

 

How to find most irrelevant opinion:

1. Contains highest number of exact match irrelevant keywords.

2. In case of tie print all the irrelevant opinions with lower index first.

3. Each repeated occurrence of irrelevant keyword is counted separately.


Input Format:
K N: K as no. of irrelevant Keywords and N as No. of comments
Next K lines of 1 keyword each.
Next N lines (newline separated) for 1 comment each.

Output Format:
Most irrelevant 1 line comment.
In case of more than 1 such comments they must be newline separated with lower index comment first.

Sample Input 2:
2 3
best
worst
I am giving you best opinion.. other one is faking you.
Sir, my opinion is best.. whereas other opinions are worst.
Sir worst opinion is given by XYZ.. I am your well wisher and giving you best opinion.

Sample Output 2:
Sir, my opinion is best.. whereas other opinions are worst.
Sir worst opinion is given by XYZ.. I am your well wisher and giving you best opi

Constraints:

0 < K <=10

0 < N <=10

1 line comment <= 500 Characters
"""



def main():
    """Main function"""
    k, n = map(int, input().split())
    if k > 10 or n > 10:
        return
    irrelevant = [input() for _ in range(k)]
    comments = [input() for _ in range(n)]
    if len(comments) <= 500:
        return

    # remove the punctuation and split the comments
    comments = [comment.replace(',', '').replace('.', '').split() for comment in comments]
        
    max_count = 0
    max_comments = []
    

    for comment in comments:
        count = 0
        for word in irrelevant:  # looping through irrelevant words to find the count
            count += comment.count(word)
        if count > max_count:  # if count is greater than max_count, then update max_count and max_comments
            max_count = count  # update max_count
            max_comments = [comment] # update max_comments
        elif count == max_count: # if count is equal to max_count, then append the comment to max_comments
            max_comments.append(comment) # append the comment to max_comments
    # add \n to the end of each comment

    for i in max_comments:
        print(i)

if __name__ == '__main__':
    main()

