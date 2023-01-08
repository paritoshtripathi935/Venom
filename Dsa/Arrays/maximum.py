"""
Given N points on a 2D plane. 
Find the maximum number of points which can be covered
by a rectangle with length x and breadth y.
A point is said to be covered by a recatangle if it lies on the sides or inside the rectangle.
N = 5
Points = [[1, 1], [2, 3], [3, 4], [2,4], [5, 5]]
X= 2
Y= 2
"""

import math

"""
class Solution {
  public:
    int maximumpoints(vector<vector<int> > arr, int n, int x, int y) {
        // code here
           vector<vector<int>>dope(1005,vector<int>(1005,0));
        int maxi1=0;
        int maxi2=0;
        for(int i=0;i<arr.size();i++){
            
            int anti=arr[i][0];
            int banti=arr[i][1];
            maxi1=max(maxi1,anti);
            maxi2=max(maxi2,banti);

            dope[anti+1][banti+1]++;
            
        }

       maxi1=max(maxi1,x);
       maxi2=max(maxi2,y);
        for(int i=1;i<=maxi1+4;i++){
            for(int j=1;j<=maxi2+4;j++){
                dope[i][j]+=(dope[i-1][j]+dope[i][j-1]-dope[i-1][j-1]);
               
                
                
            }
            
        }
        int res=0;
        for(int i=x+1;i<=maxi1+4;i++){
            
            for(int j=y+1;j<=maxi2+4;j++){
                
                    int p =dope[i][j]+dope[i-x-1][j-y-1]-dope[i-x-1][j]-dope[i][j-y-1];
              
              
                res=max(res,p);
                    
                
                   }
        }
        return res;
    }
};
"""
# write above code and change all variables names
"""
"""

def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))

    x = int(input())
    y = int(input())
    print(max_points(N, points, x, y))

if __name__ == '__main__':
    main()