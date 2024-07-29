#include <iostream>

int fib[2000000];

int main() {
    long long n, p;
    std::cin >> n >> p;

    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i < n; i++) {
        fib[i] = (fib[i - 1] + fib[i - 2]) % p;
    }

    std::cout << fib[n - 1] << std::endl;
    return 0;
}