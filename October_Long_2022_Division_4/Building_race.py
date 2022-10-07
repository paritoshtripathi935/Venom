"""
Two friends Chef and Chefina are currently on floors A and B respectively. They hear an announcement that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.
Chef can climb down XX floors per minute while Chefina can climb down YY floors per minute. Determine who will reach the ground floor first. In case both reach the ground floor together, print Both.

1≤T≤2500
1≤A,B≤100
1≤X,Y≤10

"""
def BR():
    t = int(input())
    # check for constraints
    if t < 1 or t > 2500:
        #print("Constraints not satisfied")
        return
    for i in range(t):
        a, b, x, y = map(int, input().split())
        # check for constraints
        if a < 1 or a > 100 or b < 1 or b > 100 or x < 1 or x > 10 or y < 1 or y > 10:
            #print("Constraints not satisfied")
            return
        if a == b:
            print("Both")
        elif a > b:
            if x > y:
                print("Chef")
            elif x < y:
                print("Chefina")
            else:
                print("Both")
        else:
            if x > y:
                print("Chefina")
            elif x < y:
                print("Chef")
            else:
                print("Both")

if __name__ == "__main__":
    BR()