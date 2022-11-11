#include <iostream>
#include <vector>
using namespace std;

// Write a C++ program to find the largest element of a given array of integers
int main() {
  int n;
  cin >> n;
  int arr[n];

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

    int max = arr[0];
    for (int i = 0; i < n; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
    }
}
