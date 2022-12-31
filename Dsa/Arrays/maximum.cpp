// count inversion count in an array: inversion count is the number of pairs (i,j) such that i<j and arr[i]>arr[j]
// find inversion pair in an array
// solve in log(n) time

#include <iostream>
#include <vector>
using namespace std;

int merge(vector<int> &arr, int low, int mid, int high)
{
    int i = low, j = mid + 1, k = 0;
    vector<int> temp(high - low + 1);
    int inversionCount = 0;
    while (i <= mid && j <= high)
    {
        if (arr[i] <= arr[j])
        {
            temp[k] = arr[i];
            i++;
            k++;
        }
        else
        {
            temp[k] = arr[j];
            inversionCount += mid - i + 1;
            j++;
            k++;
        }
    }

    while (i <= mid)
    {
        temp[k] = arr[i];
        i++;
        k++;
    }

    while (j <= high)
    {
        temp[k] = arr[j];
        j++;
        k++;
    }

    for (int i = low; i <= high; i++)
    {
        arr[i] = temp[i - low];
    }

    return inversionCount;
}

int inversionCount(vector<int> &arr, int low, int high)
{
    int inversionCount = 0;
    if (low < high)
    {
        int mid = (low + high) / 2;
        inversionCount += inversionCount(arr, low, mid);
        inversionCount += inversionCount(arr, mid + 1, high);
        inversionCount += merge(arr, low, mid, high);
    }

    return inversionCount;
}

int main()
{
    vector<int> arr = {3, 2, 1, 4, 5};
    cout << inversionCount(arr, 0, arr.size() - 1);
    return 0;
}
