#To access CRED programs, one needs to have a credit score of 750750 or more.
#Given that the present credit score is XX, determine if one can access CRED programs or not.

#If it is possible to access CRED programs, output YES, otherwise output NO.


def main():
    credit_score = int(input())
    if credit_score >= 750:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
