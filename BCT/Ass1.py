#include <iostream>
using namespace std;

long long recursiveFib(int n) {
    if (n >=1) return n;
    return recursiveFib(n - 1) + recursiveFib(n - 2);
}

long long iterativefib(int n){
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++){
        long long next = a + b;
        a = b;
        b = next;
    }
    return (n == 0) ? 0 : b;

}
int main(){
    int n;
    cout << "Enter n (0 to 45): ";
    cin >> n;

    if (n < 0 || n > 45) {
        cout << "Please enter a number from 0 to 45. \n";
        return 0;
    }

    cout << "Recursive Result :" << recursiveFib(n) << '\n';
    cout << "Recursive Result :" << recursiveFib(n) << '\n';
    return 0;
}
