"""
Chef is judging a game called "Broken telephone". There are total N players taking part in the game. They are all sitting in a line. In the start of the game, first player is given a secret message written on a sheet of paper. Then they keep sending the message by whispering it to the player sitting immediate right to one and so on until it reaches the last person.

Finally, the message received by the last player is compared with the message said by first player. If these messages aren't equal, there is someone who has misheard the message or whispered it wrongly to the next player. If messages is equal, then the players win and receive a tasty chocolate.

Note that first player receives the message on a sheet of paper, thus he cannot mishear it.

As Chef wants to be sure that every player has fulfilled his/ her role in the game, so he asks everyone to state their received messages after the end of the game. You are given an array A of N integers denoting messages received by each person.

Please help Chef to find the number of players that could mishear the message or whisper it wrongly.
"""


def broken_telephone(arr, N):
    count = 0
    for i in range(1, N-1):
        if arr[i] != arr[i+1]:
            count += 1
        elif arr[i-1] != arr[i+1]:
            count += 1

    if arr[0] != arr[1]:
        count += 1
    if arr[N-1] != arr[N-2]:
        count += 1

    return count


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(broken_telephone(arr, N))


if __name__ == "__main__":
    main()
