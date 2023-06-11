#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    const int arraySize = 5;
    string array[arraySize] = {"apple", "banana", "orange", "pear", "kiwi"};
    sort(array, arraay+arraySize);
    cout << "Sorted Array: " << endl;
    for(int i=0; i<arraySize; i++){
        cout << array[i] << endl;
    }
    return 0;
}