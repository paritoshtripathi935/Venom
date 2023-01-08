#include <iostream>
#include <cmath>

using namespace std;

int main() {
int t;
cin >> t; // read the number of test cases

while (t--) {
long long n;
cin >> n; // read the number N

// Find the nearest perfect square that is strictly smaller than N
long long a = sqrt(n);
while (a * a >= n) {
  a--;
}

// Find the nearest perfect square that is strictly greater than N
long long b = sqrt(n);
while (b * b <= n) {
  b++;
}

// Choose the nearest perfect square (either a or b)
if (n - a * a < b * b - n) {
  cout << a * a << endl;
} else {
  cout << b * b << endl;
}
}

return 0;
}

int binarySearch(int arr[], int l, int r, int x)
{
if (r >= l) {
int mid = l + (r - l) / 2;

// If the element is present at the middle
// itself
if (arr[mid] == x)
return mid;
}
}

int BennysArray(int arr[], int n)
{
int i, j, k, count = 0;
for (i = 0; i < n - 2; i++) {
for (j = i + 1; j < n - 1; j++) {
for (k = j + 1; k < n; k++) {
if (arr[i] > arr[j] && arr[j] > arr[k])
count++;
}
}
}
return count;
}
